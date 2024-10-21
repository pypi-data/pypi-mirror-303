import os
import shutil
from typing import Generator, NoReturn

from cnvrgv2.config import CONFIG_FOLDER_NAME
from cnvrgv2.config.routes import CVC_FILE_CHUNKS_BASE
from cnvrgv2.data.cvc.cvc_file import CvcFile
from cnvrgv2.data.cvc.cvc_metadata import COMPARE, CvcMetadata
from cnvrgv2.data.cvc.data_transfers.cvc_local_files_handler import CvcLocalFilesHandler
from cnvrgv2.data.cvc.error_messages import CVC_CHUNK_SIZE_EXCEEDED
from cnvrgv2.data.cvc.errors import CvcChunkSizeExceeded
from cnvrgv2.proxy import HTTP
from cnvrgv2.utils.json_api_format import JAF
from cnvrgv2.utils.retry import retry
from cnvrgv2.utils.storage_utils import build_cnvrgignore_spec


class CvcUploader(CvcLocalFilesHandler):
    def __init__(
            self,
            store,
            commit_sha1,
            paths,
            num_workers=40,
            queue_size=5000,
            chunk_size=10000,
            progress_bar_enabled=False
    ):
        """
        Multithreaded file downloader - download files from cvc service
        @param store: Cnvrg dataset / project object
        @param commit_sha1: string. Sha1 of the commit to upload to files to
        @param paths: list. List of paths
        @param num_workers: Number of threads to handle files
        @param queue_size: Max number of file meta to put in queue
        @param chunk_size: File meta chunk size to fetch from the server
        @param progress_bar_enabled: Boolean indicating whenever or not to print a progress bar. In use of the cli
        """
        self.commit_sha1 = commit_sha1
        self.last_successful_chunk_number = None
        self.file_chunks_path = CVC_FILE_CHUNKS_BASE.format(
            store.scope["organization"],
            store.cvc_store,
            self.commit_sha1
        )

        super().__init__(
            store=store,
            paths=paths,
            num_workers=num_workers,
            queue_size=queue_size,
            chunk_size=chunk_size,
            progress_bar_enabled=progress_bar_enabled
        )

    def _file_collector_function(self, path=None) -> Generator[list, None, NoReturn]:
        """
        Function to collect files that should be uploaded
        @param path: path of folder to collect files from (or file)
        @return: Should return array of files
        """
        files_chunk = []
        # Parses the cnvrgignore and returns a gitignore-like filter object
        ignore_spec = build_cnvrgignore_spec(self.store._config.root)

        for root, dirs, files in os.walk(path):
            if CONFIG_FOLDER_NAME in dirs:
                dirs.remove(CONFIG_FOLDER_NAME)
            rel_root_path = os.path.relpath(root, self.store._config.root) + '/'
            if not ignore_spec.match_file(rel_root_path):
                for file in files:
                    local_path = self._get_relative_path(root, file)
                    file_size = os.path.getsize(local_path)
                    if ignore_spec and ignore_spec.match_file(local_path):
                        continue

                    files_chunk.append(CvcFile(local_path=local_path, file_size=file_size))

                    if len(files_chunk) >= self.chunk_size:
                        # .copy() will return a copy files_chunk, so that .clear() will not clear
                        # the chunk still in use by the upload threads
                        yield files_chunk.copy()
                        files_chunk.clear()

        # leftovers
        if len(files_chunk):
            yield files_chunk.copy()
            # .copy() will return a copy files_chunk, so that .clear() will not clear
            # the chunk still in use by the upload threads
            files_chunk.clear()

    def _file_handler_function(self, cvc_file, progress_bar=None):
        """
        Function that uploads single file and creates its metadata
        @param cvc_file: object. CvcFile object
        @return: None
        """
        local_path = cvc_file.local_path

        # Shared code running for new files and updated files
        if cvc_file.metadata_status in [COMPARE.DOESNT_EXIST, COMPARE.DIFFERENT]:
            object_path = self._create_object_storage_path(local_path)
            self.storage_client.upload_single_file(local_path, object_path, progress_bar=progress_bar)

            # (re)create the metadata object for the file
            metadata_path = CvcMetadata.meta_path(cvc_file.local_path)
            cvc_file.metadata = CvcMetadata(metadata_path)
            cvc_file.metadata.object_path = object_path
            cvc_file.metadata.set_update_time()

        # Block for files already in server
        else:
            pass

        # Code running only for new files
        if cvc_file.metadata_status == COMPARE.DOESNT_EXIST:
            cvc_file.metadata.set_creation_time()

        # Anyway, update the commit
        cvc_file.metadata.commit_sha1 = self.commit_sha1
        cvc_file.metadata.save()

    def _create_object_storage_path(self, local_path):
        """
        Creates a path to upload the file to
        @param local_path: string. The local path of the file
        @return: The path to upload the file to in the object_storage
        """
        return os.path.join(self.store.slug, self.commit_sha1, local_path)

    @retry()
    def _handle_file_progress_function(self, files_chunk, retry_attempt_number=None):
        """
        Adds file to chunk. when chunk is big enough, send to cvc server
        @param files_chunk: dict. Dictionary that represents a chunk of files
        @param retry_attempt_number: The attempt number that this function is run through the retry mechanism.
                                    This param is automatically injected by @retry(), Do not pass a value.
        @return: None
        """
        if len(files_chunk) > self.chunk_size:
            raise CvcChunkSizeExceeded(CVC_CHUNK_SIZE_EXCEEDED)

        if len(files_chunk):
            headers = None
            data = {
                "files": files_chunk
            }

            if retry_attempt_number:
                headers = {
                    "retry": "true"
                }

                if self.last_successful_chunk_number:
                    data["override_chunk_number"] = self.last_successful_chunk_number + 1
                else:
                    data["override_chunk_number"] = 0

            result = self.store._proxy.call_api(
                route=self.file_chunks_path,
                http_method=HTTP.POST,
                headers=headers,
                payload=JAF.serialize(type="cvc", attributes=data),
                retry_enabled=False
            )

            self.last_successful_chunk_number = result.attributes["chunk_number"]

    def _get_relative_path(self, directory_path, file_name):
        """
        This function normalizes the path of a file so that it will be relative to the store's root folder.
        @param directory_path: string. Full path of the directory containing the file
        @param file_name: string. File name
        @return: The path of the file relatively to the store's root folder
        """
        fullpath = os.path.join(directory_path, file_name)
        return os.path.relpath(fullpath, self.store._config.root)

    def _metadata_files_deleter_function(self):
        """
        Iterates over the metadata folder and removes orphan metadata files.
        @return: None
        """
        metadata_folder = os.path.join(CONFIG_FOLDER_NAME, CvcMetadata.METADATA_FOLDER_NAME)

        for root, dirs, metadata_paths in os.walk(metadata_folder):
            local_root_name = root.replace(metadata_folder, '').strip("/")
            if local_root_name and not os.path.exists(local_root_name):
                shutil.rmtree(root)
            for dir_name in dirs:
                meta_dir_path = os.path.join(root, dir_name)
                local_dir_path = os.path.join(local_root_name, dir_name)
                if not os.path.exists(local_dir_path):
                    shutil.rmtree(meta_dir_path)
            for metadata in metadata_paths:
                metadata_path = os.path.join(root, metadata)
                metadata_file = CvcMetadata(metadata_path, load_metadata=False)
                if metadata_file.is_orphan:
                    os.remove(metadata_path)
