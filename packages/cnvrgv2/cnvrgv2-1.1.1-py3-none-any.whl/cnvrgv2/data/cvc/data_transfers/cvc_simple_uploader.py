import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from typing import Generator, NoReturn

from cnvrgv2.config import CONFIG_FOLDER_NAME
from cnvrgv2.data.cvc.cvc_file import CvcFile
from cnvrgv2.data.cvc.cvc_metadata import COMPARE, CvcMetadata
from cnvrgv2.data.cvc.error_messages import CVC_CHUNK_SIZE_EXCEEDED
from cnvrgv2.data.cvc.errors import CvcChunkSizeExceeded
from cnvrgv2.data.cvc.routes import CVC_FILE_CHUNKS_BASE
from cnvrgv2.proxy import HTTP
from cnvrgv2.utils.json_api_format import JAF
from cnvrgv2.utils.storage_utils import append_trailing_slash


class CvcSimpleUploader:
    def __init__(self, store, commit_sha1, paths, chunk_size=10000, num_workers=40):
        """
        Multithreaded file uploader - upload files to storage & cvc service
        @param store: Cnvrg dataset / project object
        @param commit_sha1: string. Sha1 of the commit to upload to files to
        @param paths: list. List of paths
        @param chunk_size: Max chunk size to upload to the server
        @param num_workers: Number of threads to handle files
        """
        self.commit_sha1 = commit_sha1
        self.file_chunks_path = CVC_FILE_CHUNKS_BASE.format(store.slug, self.commit_sha1)
        self.paths = paths
        self.store = store
        self.chunk_size = chunk_size
        self.storage_client = self.store.storage_client
        self.num_workers = num_workers

    def upload(self):
        """
        Uploads all the files in local dir to the server
        @return: None
        """
        data_owner_root = append_trailing_slash(self.store.config.root) if self.store.config.root else ''
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            for fullpath in self.paths:
                # TODO: Support files when implementing put_files before production
                if os.path.isfile(fullpath):
                    print("Cvc doesn't support uploading separated files yet. skipping {}".format(fullpath))
                    continue

                # Normalize fullpath to be relative to the working directory
                path = fullpath.replace(data_owner_root, "")
                folder_collector_generator = self._file_collector_function(path)

                while True:
                    try:
                        collected_files_chunk = next(folder_collector_generator)
                        executor.submit(self._upload_chunk, collected_files_chunk)
                    except StopIteration:
                        # Meaning the generator is exhausted. No more files for the given path
                        break

    def _upload_chunk(self, chunk):
        with ThreadPool(processes=self.num_workers) as pool:
            pool.map(self._upload_file_to_storage, chunk)
        self._upload_chunk_to_cvc(chunk)

    def _file_collector_function(self, path=None) -> Generator[list, None, NoReturn]:
        """
        Function to collect local files that should be uploaded
        @param path: path of folder to upload
        @return: Returns a generator. Yields chunk of files to upload
        """
        files_chunk = []
        for root, dirs, files in os.walk(path):
            if CONFIG_FOLDER_NAME in dirs:
                dirs.remove(CONFIG_FOLDER_NAME)

            for file in files:
                local_path = self._get_relative_path(root, file)
                files_chunk.append(CvcFile(local_path))

                if len(files_chunk) >= self.chunk_size:
                    # .copy() will return a copy files_chunk, so that .clear() will not clear
                    # the chunk still in use by the upload threads
                    yield files_chunk.copy()
                    files_chunk.clear()

        # leftovers
        if len(files_chunk):
            # .copy() will return a copy files_chunk, so that .clear() will not clear
            # the chunk still in use by the upload threads
            yield files_chunk.copy()
            files_chunk.clear()

    def _upload_file_to_storage(self, cvc_file):
        """
        Function that uploads single file and creates its metadata
        @param cvc_file: object. CvcFile object
        @return: None
        """
        local_path = cvc_file.local_path
        if cvc_file.metadata_status in [COMPARE.DOESNT_EXIST, COMPARE.DIFFERENT]:
            object_path = self._create_object_storage_path(local_path)
            self.storage_client.upload_single_file(local_path, object_path)

            # (re)create the metadata object for the file
            cvc_file.metadata = CvcMetadata(cvc_file.local_path)
            cvc_file.metadata.object_path = object_path

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

    def _upload_chunk_to_cvc(self, files_chunk):
        """
        Adds file to chunk. when chunk is big enough, send to cvc server
        @param files_chunk: dict. Dictionary that represents a chunk of cvc_files
        @return: None
        """
        if len(files_chunk) > self.chunk_size:
            raise CvcChunkSizeExceeded(CVC_CHUNK_SIZE_EXCEEDED)

        if len(files_chunk):
            files = {cvc_file.local_path: {'object_path': cvc_file.metadata.object_path} for cvc_file in files_chunk}
            data = {
                "files": files
            }

            self.store.proxy.call_api(
                route=self.file_chunks_path,
                http_method=HTTP.POST,
                payload=JAF.serialize(type="cvc", attributes=data)
            )

    def _get_relative_path(self, directory_path, file_name):
        """
        This function normalizes the path of a file so that it will be relative to the store's root folder.
        @param directory_path: string. Full path of the directory containing the file
        @param file_name: string. File name
        @return: The path of the file relatively to the store's root folder
        """
        fullpath = os.path.join(directory_path, file_name)
        return os.path.relpath(fullpath, self.store.config.root)
