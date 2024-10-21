import os
from glob import iglob
from typing import Generator, NoReturn

from cnvrgv2.config import CONFIG_FOLDER_NAME
from cnvrgv2.config.routes import CVC_FILE_CHUNKS_BASE
from cnvrgv2.data.cvc.cvc_file import CvcFile
from cnvrgv2.data.cvc.cvc_metadata import CvcMetadata
from cnvrgv2.data.cvc.data_transfers.cvc_local_files_handler import CvcLocalFilesHandler
from cnvrgv2.data.cvc.error_messages import CVC_CHUNK_SIZE_EXCEEDED
from cnvrgv2.data.cvc.errors import CvcChunkSizeExceeded
from cnvrgv2.proxy import HTTP
from cnvrgv2.utils.json_api_format import JAF
from cnvrgv2.utils.storage_utils import (get_relative_path, path_is_wildcard)


class CvcPutFiles(CvcLocalFilesHandler):
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
        Multithreaded file uploader - upload files to cvc service - without context
        @param store: Cnvrg dataset / project object
        @param commit_sha1: string. Sha1 of the commit to upload to files to
        @param paths: list. List of paths
        @param num_workers: Number of threads to handle files
        @param queue_size: Max number of file meta to put in queue
        @param chunk_size: File meta chunk size to fetch from the server
        @param progress_bar_enabled: Boolean indicating whenever or not to print a progress bar. In use of the cli
        """
        self.commit_sha1 = commit_sha1
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
            progress_bar_enabled=progress_bar_enabled,
            progress_bar_message="Uploading"
        )

    def _file_collector_function(self, path=None) -> Generator[list, None, NoReturn]:
        """
        Function to collect files that should be uploaded
        @return: Should return array of files
        """
        files_chunk = []
        # Calculate which folder we should traverse as part of the regex
        is_wildcard = path_is_wildcard(path)
        if is_wildcard:
            # if is wildcard, collect all relevant files
            for file_path in iglob(path):
                files_chunk.append(CvcFile(file_path))
                if len(files_chunk) >= self.chunk_size:
                    # .copy() will return a copy files_chunk, so that .clear() will not clear
                    # the chunk still in use by the upload threads
                    yield files_chunk.copy()
                    files_chunk.clear()
        else:
            is_dir = os.path.isdir(path)
            is_file = os.path.isfile(path)
            if is_dir:
                for root, dirs, files in os.walk(path):
                    if CONFIG_FOLDER_NAME in dirs:
                        dirs.remove(CONFIG_FOLDER_NAME)
                    for file in files:
                        self._file_collector(root=root, file=file, files_chunk=files_chunk)
                        if len(files_chunk) >= self.chunk_size:
                            # .copy() will return a copy files_chunk, so that .clear() will not clear
                            # the chunk still in use by the upload threads
                            yield files_chunk.copy()
                            files_chunk.clear()
            elif is_file:
                self._file_collector(root=None, file=path, files_chunk=files_chunk)
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

    def _file_collector(self, root, file, files_chunk):
        """
        Helper function to collect local files for a given path (directory or file)
        @param root: root of folder to upload
        @param file: local path of file
        @param files_chunk: array of files to add to
        @return: appends new file path to files_chunk
        """
        local_path = file
        if root:
            local_path = get_relative_path(os.path.join(root, file))

        files_chunk.append(CvcFile(local_path))

    def _file_handler_function(self, cvc_file, progress_bar=None):
        """
        Function that uploads single file to the storage and creates its metadata (we need it to save object_path)
        @param cvc_file: object. CvcFile object
        @return: None
        """
        local_path = cvc_file.local_path
        object_path = self._create_object_storage_path(local_path)
        self.storage_client.upload_single_file(local_path, object_path, progress_bar=progress_bar)

        metadata_path = CvcMetadata.meta_path(cvc_file.local_path)
        cvc_file.metadata = CvcMetadata(metadata_path)
        cvc_file.metadata.object_path = object_path
        cvc_file.metadata.set_creation_time()
        cvc_file.metadata.set_update_time()

    def _create_object_storage_path(self, local_path):
        """
        Creates a path to upload the file to
        @param local_path: string. The local path of the file
        @return: The path to upload the file to in the object_storage
        """
        return os.path.join(self.store.slug, self.commit_sha1, local_path)

    def _handle_file_progress_function(self, files_chunk):
        """
        Sends file chunk to cvc server
        @param files_chunk: dict. Dictionary that represents a chunk of files
        @return: None
        """
        if len(files_chunk) > self.chunk_size:
            raise CvcChunkSizeExceeded(CVC_CHUNK_SIZE_EXCEEDED)

        if len(files_chunk):

            data = {
                "files": files_chunk
            }

            self.store._proxy.call_api(
                route=self.file_chunks_path,
                http_method=HTTP.PUT,
                payload=JAF.serialize(type="cvc", attributes=data)
            )

    def _metadata_files_deleter_function(self):
        """
        We don't handle local deletions with put_files, since it occurs out of context
        @return: None
        """
        pass
