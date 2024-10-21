import os

from cnvrgv2.data.cvc.cvc_metadata import COMPARE, CvcMetadata


class CvcFile:
    def __init__(self, local_path, file_size=0):
        self.local_path = local_path
        self._metadata_path = CvcMetadata.meta_path(self.local_path)  # The expected path for the metadata file
        self.metadata = CvcMetadata(metadata_path=self._metadata_path)
        self.file_size = file_size
        if not file_size:
            if os.path.exists(local_path):
                self.file_size = os.path.getsize(local_path)

        self._metadata_status = None

    @property
    def metadata_status(self):
        if not self._metadata_status:
            if os.path.exists(self._metadata_path):
                if os.path.getmtime(self.local_path) > os.path.getmtime(self._metadata_path):
                    self._metadata_status = COMPARE.DIFFERENT
                else:
                    self._metadata_status = COMPARE.SAME

            else:
                self._metadata_status = COMPARE.DOESNT_EXIST
        return self._metadata_status
