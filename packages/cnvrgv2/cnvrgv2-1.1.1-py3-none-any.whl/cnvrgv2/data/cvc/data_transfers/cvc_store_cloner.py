import requests

from cnvrgv2.config import routes
from cnvrgv2.data.cvc.cvc_file import CvcFile
from cnvrgv2.data.cvc.data_transfers.cvc_remote_files_handler import CvcRemoteFilesHandler
from cnvrgv2.errors import CnvrgHttpError
from cnvrgv2.proxy import HTTP
from cnvrgv2.utils.url_utils import urljoin


class CvcStoreCloner(CvcRemoteFilesHandler):
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
        @param chunk_size: File meta chunk size to fetch from the server
        """
        self.commit_sha1 = commit_sha1
        base_route = routes.ORGANIZATION_BASE.format(store.scope["organization"])
        route = urljoin(
            base_route,
            'cvc/stores/{}/commits/{}/file-chunks?with_total_files_size=true'.format(store.cvc_store, commit_sha1)
        )
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
            progress_bar_message="Cloning"
        )

    def _collector_function(self, chunk_number=None) -> list:
        """
        Function to collect files that should be downloaded
        @param chunk_number: int. The sequence of the chunk to fetch
        @return: Should return array of cvc file objects
        """
        try:
            files = []
            base_route = routes.ORGANIZATION_BASE.format(self.store.scope["organization"])
            route = urljoin(
                base_route,
                'cvc/stores/{}/commits/{}/file-chunks/{}'.format(self.store.cvc_store, self.commit_sha1, chunk_number)
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

    def _handle_file_function(self, cvc_file, progress_bar=None):
        """
        Function that download single file
        @param cvc_file: obj. A CvcFile object
        @param progress_bar: A progress bar object to be used during the download
        @return: None
        """
        self.storage_client.download_single_file(cvc_file.local_path, cvc_file.metadata.object_path,
                                                 progress_bar=progress_bar)
        cvc_file.metadata.commit_sha1 = self.commit_sha1
        cvc_file.metadata.save()

        self.handle_queue.task_done()
        self.progress_queue.put(cvc_file)
