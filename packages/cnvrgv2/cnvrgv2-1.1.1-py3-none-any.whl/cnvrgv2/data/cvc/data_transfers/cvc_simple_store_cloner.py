import os
from multiprocessing.pool import ThreadPool

import requests

from cnvrgv2.data.cvc.cvc_file import CvcFile
from cnvrgv2.data.cvc.error_messages import CVC_FAILED_TO_FETCH_CHUNK, CVC_GENERAL_DOWNLOAD_ERROR, CVC_RETRIES_EXCEEDED
from cnvrgv2.data.cvc.routes import CVC_FILE_CHUNKS_BASE
from cnvrgv2.errors import CnvrgHttpError, CnvrgRetryError
from cnvrgv2.proxy import HTTP


class CvcSimpleStoreCloner:
    def __init__(self, store, commit_sha1, num_workers=40):
        self.store = store
        self.storage_client = self.store.storage_client
        self.commit_sha1 = commit_sha1
        self.file_chunks_path = CVC_FILE_CHUNKS_BASE.format(self.store.slug, self.commit_sha1)
        self.num_workers = num_workers

    def download(self):
        """
        Downloads all the files in the commit and store that were specified at the constructor
        @return: None
        """
        old_working_directory = os.getcwd()
        os.chdir(self.store.slug)
        try:
            next_chunk = 0
            while next_chunk >= 0:
                files = self._get_file_chunk(next_chunk)
                if not files:
                    next_chunk = -1
                    continue

                self._download_from_storage(files)
                next_chunk += 1
        finally:
            os.chdir(old_working_directory)

    def _get_file_chunk(self, chunk):
        """
        Gets the data of the given chunk
        @param chunk: Integer. The chunk number to fetch
        @return: List of CvcFile objects, or None if chunk doesn't exist
        """
        try:
            files = []
            file_chunk_path = os.path.join(self.file_chunks_path, str(chunk))
            chunk_data = self.store.proxy.call_api(
                route=file_chunk_path,
                http_method=HTTP.GET
            ).attributes.get("files")

            for local_path, metadata in chunk_data.items():
                cvc_file = CvcFile(local_path=local_path)
                cvc_file.metadata.object_path = metadata["object_path"]
                files.append(cvc_file)

            return files

        except CnvrgHttpError as e:
            # Reached last chunk
            if e.status_code == requests.codes.not_found:
                return None

        except Exception as e:
            # TODO: Consult product regarding desired behaviour on failures. Until then keep printing and skipping
            print(CVC_FAILED_TO_FETCH_CHUNK.format(chunk, str(e)))

    def _download_from_storage(self, files):
        """
        Concurrently downloads the given files
        @param files: dict. Metadata of the files to download
        @return: None
        """
        with ThreadPool(processes=self.num_workers) as pool:
            pool.map(self._download_file, files)

    def _download_file(self, file):
        """
        Function that download single file and creates the corresponding metadata file.
        This function is meant to be called asynchronously
        @param file: dict: A dictionary that contains the local_path and the metadata of the file
        @return: None
        """
        try:
            self.storage_client.download_single_file(file.local_path, file.metadata.object_path)
            file.metadata.commit_sha1 = self.commit_sha1
            file.metadata.save()

        # TODO: Consult product regarding desired behaviour on failures. Until then keep printing and skipping
        except CnvrgRetryError:
            print(CVC_RETRIES_EXCEEDED.format(file.local_path))
        except Exception as e:
            print(CVC_GENERAL_DOWNLOAD_ERROR.format(file.local_path, str(e)))
