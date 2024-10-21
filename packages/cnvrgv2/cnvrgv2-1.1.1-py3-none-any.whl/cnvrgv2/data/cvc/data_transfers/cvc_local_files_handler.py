import threading
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Empty, Full, Queue
from typing import Generator, NoReturn

from cnvrgv2.cli.utils.messages import PROGRESS_BAR_UPLOAD_CALC
from cnvrgv2.cli.utils.progress_bar_utils import init_progress_bar_for_cli
from cnvrgv2.data.clients.storage_client_factory import storage_client_factory
from cnvrgv2.data.cvc.cvc_metadata import COMPARE
from cnvrgv2.utils.storage_utils import append_trailing_slash


class CvcLocalFilesHandler:
    def __init__(
            self,
            store,
            paths,
            num_workers=40,
            chunk_size=10000,
            queue_size=5000,
            progress_bar_enabled=False,
            progress_bar_message=""
    ):
        """
        Multithreaded local file handler base class
        @param store: The store object
        @param paths: [Generator] that lists paths to upload
        @param num_workers: Number of threads to use for concurrent file handling
        @param chunk_size: File meta chunk size to fetch from the server
        @param queue_size: Max number of file meta to put in queue
        @param progress_bar_enabled: Boolean indicating whenever or not to print a progress bar. In use of the cli
        """
        # Init the storage client
        self.store = store
        self.storage_client = storage_client_factory(refresh_function=self.store.storage_meta_refresh_function())
        # Init helper vars
        self.queue_size = queue_size
        self.chunk_size = chunk_size
        self.path_generator = paths
        self.progress_bar_enabled = progress_bar_enabled
        self.errors = []
        self.progress_bar = None

        # Init progress bar messages
        self.progress_bar_message = progress_bar_message

        # Init file queues
        self.progress_queue = Queue(self.queue_size)
        self.handle_queue = Queue(self.queue_size)

        # Create a thread event in order to exit handling when needed
        self.handling_active = threading.Event()
        self.handling_active.set()

        self._in_progress = threading.Event()
        self._in_progress.set()

        # Create a thread-safe lock
        self.progress_lock = threading.Lock()

        self.total_files = 0
        self.total_files_count_finished = False
        self.handled_files = 0

        self.handler_threads = []

        # Create collector thread which sends file chunks to the server
        self.collector_thread = threading.Thread(target=self.file_collector)
        # Create progress thread which tracks the upload progress
        self.progress_thread = threading.Thread(target=self.task_progress)
        self.deleter_thread = threading.Thread(target=self.metadata_file_deleter)

        self.collector_thread.start()
        self.deleter_thread.start()
        # self.progress_thread should be last, because it is the one that calls the clear
        # (all threads should start before the clear)
        self.progress_thread.start()

        # Create downloader threads to parallelize file handling
        for i in range(num_workers):
            t = threading.Thread(target=self.file_handler)
            t.start()
            self.handler_threads.append(t)

    def clear(self):
        """
        Clear the threads used to upload files
        @return: none
        """
        # Clear download threads
        try:
            self.handling_active.clear()
            self.collector_thread.join()
            self.deleter_thread.join()
        except RuntimeError:
            # If one of the threads has not started, it will throw an error when trying to join
            pass

        try:
            for t in self.handler_threads:
                t.join()

            if self.progress_bar_enabled and self.progress_bar:
                self.progress_bar.finish()

        except Exception:
            pass
        finally:
            self._in_progress.clear()

    @property
    def in_progress(self):
        """
        Property used to check if the upload is still in progress
        @return: Boolean
        """
        return self._in_progress.is_set()

    def file_collector(self):
        """
        The function that handles collecting files metadata from the server
        @return: None
        """
        data_owner_root = append_trailing_slash(self.store._config.root) if self.store._config.root else ''
        total_size = 0
        # Go over each path (folder), collect file chunks to upload, and add them to the handle_queue
        with ThreadPoolExecutor() as executor:
            for fullpath in self.path_generator:

                # Normalize fullpath to be relative to the working directory
                path = fullpath.replace(data_owner_root, "")
                folder_collector_generator = self._file_collector_function(path)
                while True:
                    try:
                        collected_files_chunk = next(folder_collector_generator)
                        self.total_files += len(collected_files_chunk)
                        total_size += sum(
                            [file.file_size for file in collected_files_chunk
                             if file.metadata_status in [COMPARE.DOESNT_EXIST, COMPARE.DIFFERENT]]
                        )
                        if self.progress_bar_enabled and total_size:
                            if not self.progress_bar:
                                self.progress_bar = init_progress_bar_for_cli(
                                    self.progress_bar_message,
                                    total_size,
                                    ready=False,
                                    spinner_text=PROGRESS_BAR_UPLOAD_CALC
                                )
                        # Parallelize the add to handle queue part,
                        # to prevent stalling the next call of _file_collector_function
                        executor.submit(self._add_chunk_to_handle_queue, collected_files_chunk)
                    except StopIteration:
                        # Meaning the generator is exhausted. No more files for the given path
                        break

        self.total_files_count_finished = True

        # Complete the progress bar initialization only after we finish with calculating the total upload size
        if self.progress_bar_enabled and self.progress_bar and total_size:
            self.progress_bar.finish_init(total_size)

    def _add_chunk_to_handle_queue(self, chunk):
        """
        Attempt to put the new files in the upload queue, non-blocking in case we want to stop the upload
        @param chunk: list. Files to add to the handle_queue
        @return: None
        """
        for cvc_file in chunk:
            while self.handling_active.is_set():
                try:
                    self.handle_queue.put_nowait(cvc_file)
                    break
                except Full:
                    time.sleep(0.5)

    def metadata_file_deleter(self):
        """
        Deletes metadata files that belong to files that got deleted by the user
        @return: None
        """
        self._metadata_files_deleter_function()

    def file_handler(self):
        """
        Handles uploading files to the relevant object storage
        @return: None
        """
        # Run as long as we have files to upload
        while self.handling_active.is_set():
            try:
                # Get file non-blocking way, otherwise thread will hang forever
                cvc_file = self.handle_queue.get_nowait()
                self._file_handler_function(cvc_file, self.progress_bar)
                self.handle_queue.task_done()

                self.progress_queue.put(cvc_file)
            except Empty:
                time.sleep(0.5)
            except Exception as e:
                self.errors.append(e)
                with self.progress_lock:
                    self.handled_files += 1

    def task_progress(self):
        """
        Handles the upload progress and confirming file uploads to the server
        @return: None
        """
        pending_files_chunk = {}

        while self.total_files_count_finished is False or self.handled_files < self.total_files:
            try:
                cvc_file = self.progress_queue.get_nowait()
                pending_files_chunk[cvc_file.local_path] = {
                    "object_path": cvc_file.metadata.object_path,
                    "file_size": cvc_file.file_size,
                    "created_at": cvc_file.metadata.created_at,
                    "updated_at": cvc_file.metadata.updated_at
                }

                with self.progress_lock:
                    self.handled_files += 1

                if len(pending_files_chunk) >= self.chunk_size:
                    self._handle_file_progress_function(pending_files_chunk)
                    pending_files_chunk.clear()

            except Empty:
                time.sleep(0.5)

        # leftovers
        if len(pending_files_chunk):
            self._handle_file_progress_function(pending_files_chunk)

        self.clear()

    def _handle_file_progress_function(self, cvc_file):
        """
        Base function to progress the task
        @param cvc_file: object. A CvcFile object
        @return: None
        """
        pass

    def _file_handler_function(self, file, progress_bar=None):
        """
        Base function to handle single file
        @param file: dict. Dictionary containing the local file path to file compare result (compare to metadata file)
        @return: None
        """
        pass

    def _file_collector_function(self, path) -> Generator[list, None, NoReturn]:
        """
        Base function to collect files metadata from server
        @return: Should return array of files metadata
        """
        pass

    def _metadata_files_deleter_function(self):
        """
        Base function for deleting metadata files that belong to files that got deleted by the user
        @return: None
        """
        pass
