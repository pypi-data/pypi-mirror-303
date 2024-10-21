import json
import os

import requests

from cnvrgv2.config import CONFIG_FOLDER_NAME
from cnvrgv2.config.routes import CVC_FILE_CHUNK_BASE, CVC_FILE_CHUNKS_BASE
from cnvrgv2.data.cvc.cvc_file import CvcFile
from cnvrgv2.data.cvc.cvc_metadata import COMPARE, CvcMetadata
from cnvrgv2.data.cvc.data_transfers.cvc_remote_files_handler import CvcRemoteFilesHandler
from cnvrgv2.errors import CnvrgHttpError
from cnvrgv2.proxy import HTTP
from cnvrgv2.utils.converters import convert_bytes
from cnvrgv2.utils.url_utils import urljoin


class CvcDownloader(CvcRemoteFilesHandler):
    def __init__(
            self,
            store,
            commit_sha1,
            num_workers=40,
            queue_size=5000,
            progress_bar_enabled=False
    ):
        """
        Multithreaded file downloader - download files from cvc service
        @param store: Cnvrg dataset / project object
        @param commit_sha1: Sha1 of the commit to clone
        @param num_workers: Number of threads to handle files
        @param queue_size: Max number of file meta to put in queue
        @param progress_bar_enabled: Boolean indicating whenever or not to print a progress bar. In use of the cli

        """
        self.commit_sha1 = commit_sha1
        self.file_chunks_path = CVC_FILE_CHUNKS_BASE.format(
            store.scope["organization"],
            store.cvc_store,
            self.commit_sha1
        )
        route = urljoin(self.file_chunks_path, '?with_total_files_size=true')
        response = store._proxy.call_api(
            route=route,
            http_method=HTTP.GET
        )
        # If commit has no file chunks, no meta is returned
        if response.meta:
            total_files = response.meta.get("total_files_count", 0)
            total_files_size = response.meta.get("total_files_size", 0)
        else:
            total_files = 0
            total_files_size = 0

        super().__init__(
            store,
            total_files,
            total_files_size=total_files_size,
            num_workers=num_workers,
            queue_size=queue_size,
            progress_bar_enabled=progress_bar_enabled,
            progress_bar_message="Downloading"
        )

    def _collector_function(self, chunk_number=None) -> list:
        """
        Function to collect files that should be downloaded
        @param chunk_number: The chunk_number to be downloaded
        @return: Should return array of files metadata
        """
        try:
            files = []
            route = CVC_FILE_CHUNK_BASE.format(
                self.store.scope["organization"],
                self.store.cvc_store,
                self.commit_sha1,
                str(chunk_number)
            )

            chunk_data = self.store._proxy.call_api(
                route=route,
                http_method=HTTP.GET
            ).attributes["files"]

            for local_path, metadata in chunk_data.items():
                relative_path = "{}/{}".format(self.store.working_dir, local_path)
                cvc_file = CvcFile(local_path=relative_path)
                cvc_file.metadata.object_path = metadata["object_path"]
                cvc_file.metadata.created_at = metadata["created_at"]
                cvc_file.metadata.updated_at = metadata["updated_at"]
                files.append(cvc_file)

            return files

        except CnvrgHttpError as e:
            if e.status_code == requests.codes.not_found:
                # This will indicate the calling function that there are no more files to collect
                return []
            else:
                raise e

    def _handle_file_function(self, file, progress_bar=None):
        """
        Function that download single file
        @param file: dict: A dictionary that contains the local_path and the metadata of the file
        @param progress_bar: A progress bar object to be used during the download
        @return: None
        """
        local_path = file.local_path

        # if file doesn't exist locally, download it
        if not os.path.exists(local_path):
            self.storage_client.download_single_file(
                local_path,
                file.metadata.object_path,
                progress_bar=progress_bar
            )
        else:
            # if local_path exists, check if metadata exists for this file
            meta_path = file.metadata.metadata_path
            if file.metadata_status is not COMPARE.DOESNT_EXIST:
                # if metadata exists, check if object path is the same
                with open(meta_path, "r") as f:
                    data = f.read()
                    old_metadata_json = json.loads(data)
                    old_object_path = old_metadata_json['object_path']
                    if old_object_path != file.metadata.object_path:
                        # if path is different, we need to download the file again
                        # delete local file
                        os.remove(local_path)
                        self.storage_client.download_single_file(
                            local_path,
                            file.metadata.object_path,
                            progress_bar=progress_bar
                        )
                    else:
                        if progress_bar:
                            # If file changed locally, we do not override the changes.
                            # But we update the progress bar
                            converted_bytes, unit = convert_bytes(file.file_size, progress_bar.unit)
                            progress_bar.throttled_next(converted_bytes)
            else:
                # If file already exists, but no metadata, download again,
                # since there is no way to know if it is the right version, no object path to compare with.
                # This block covers an edge case that should not happen
                os.remove(local_path)
                self.storage_client.download_single_file(
                    local_path,
                    file.metadata.object_path,
                    progress_bar=progress_bar
                )

        # In any case we need a correct version of the metadata file. Hence, update the commit and save.
        file.metadata.commit_sha1 = self.commit_sha1
        file.metadata.save()

        self.handle_queue.task_done()
        self.progress_queue.put(file)

    def cvc_file_deleter(self, commit_sha1):
        """
        Deletes local files that have been deleted in the latest commit
        Iterates over the metadata folder and removes files that are not aligned with the latest commit.
        @return: None
        """
        metadata_folder = os.path.join(CONFIG_FOLDER_NAME, CvcMetadata.METADATA_FOLDER_NAME)

        for root, dirs, metadata_paths in os.walk(metadata_folder):
            for metadata in metadata_paths:
                metadata_path = os.path.join(root, metadata)
                metadata_file = CvcMetadata(metadata_path)

                if metadata_file.commit_sha1 != commit_sha1:
                    # if commit is different,
                    # this means that the file does not exist in the latest commit and needs to be deleted
                    if os.path.exists(metadata_file.local_path):
                        os.remove(metadata_file.local_path)
                    os.remove(metadata_path)
