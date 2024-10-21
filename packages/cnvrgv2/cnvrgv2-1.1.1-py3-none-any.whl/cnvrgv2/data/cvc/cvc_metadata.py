import json
import os
from datetime import datetime
from json import JSONDecodeError
from pathlib import Path

from cnvrgv2.config import CONFIG_FOLDER_NAME
from cnvrgv2.data.cvc.error_messages import CVC_METADATA_FILE_MISSING_KEY
from cnvrgv2.errors import CnvrgFileError


class COMPARE:
    DOESNT_EXIST = 0
    SAME = 1
    DIFFERENT = 2


class CvcMetadata:
    METADATA_FOLDER_NAME = ".metadata"
    METADATA_FILE_EXTENSION = ".cnvrg"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, metadata_path, load_metadata=True):
        """
        Initiates a CvcMetadata object. Will try to fill fields from metadata file, if exists
        @param metadata_path: string. The expected path for the metadata file (even if it doesn't exist yet)
        @param load_metadata: bool. Whenever to load fields from the metadata file (if exists), True by default
        """
        self.metadata_path = metadata_path
        self.local_path = self._local_file_path(self.metadata_path)  # The expected path for the local file
        self.commit_sha1 = None
        self.object_path = None
        self.created_at = None
        self.updated_at = None

        if os.path.exists(self.metadata_path) and load_metadata:
            try:
                with open(self.metadata_path, "r") as metadata_file:
                    file_meta = json.load(metadata_file)
                    self.object_path = file_meta["object_path"]
                    self.commit_sha1 = file_meta["commit_sha1"]
                    self.created_at = file_meta["created_at"]
                    self.updated_at = file_meta["updated_at"]
            except JSONDecodeError:  # Empty file. handle like no file
                pass
            except KeyError as e:
                raise CnvrgFileError(CVC_METADATA_FILE_MISSING_KEY.format(str(e)))

    @property
    def is_orphan(self):
        """
        Checks if the local file exists
        @return: bool. Whenever a corresponding local file exists
        """
        if os.path.exists(self.local_path):
            return False
        else:
            return True

    def set_creation_time(self):
        local_path = Path(self.local_path)
        if local_path.exists():
            stat = local_path.stat()
            created_timestamp = stat.st_birthtime if hasattr(stat, "st_birthtime") else stat.st_ctime
            created = datetime.fromtimestamp(created_timestamp).strftime(CvcMetadata.DATE_FORMAT)
            self.created_at = created

    def set_update_time(self):
        local_path = Path(self.local_path)
        if local_path.exists():
            modified = datetime.fromtimestamp(local_path.stat().st_mtime).strftime(CvcMetadata.DATE_FORMAT)
            self.updated_at = modified

    def save(self):
        """
        Saves the current object as a metadata file
        @return: None
        """

        data = {
            "commit_sha1": self.commit_sha1,
            "object_path": self.object_path,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        os.makedirs(os.path.dirname(self.metadata_path), exist_ok=True)

        with open(self.metadata_path, "w") as f:
            f.write(json.dumps(data))

    @staticmethod
    def meta_path(local_path) -> str:
        """
        Calculates the expected path of the metadata file
        @param local_path: string. The path of the local file to generate the metadata path for
        @return: str. The expected metadata path
        """
        metadata_folder_prefix = os.path.join(CONFIG_FOLDER_NAME, CvcMetadata.METADATA_FOLDER_NAME)
        return "{}/{}{}".format(metadata_folder_prefix, local_path, CvcMetadata.METADATA_FILE_EXTENSION)

    @staticmethod
    def _local_file_path(metadata_path):
        metadata_folder_prefix = os.path.join(CONFIG_FOLDER_NAME, CvcMetadata.METADATA_FOLDER_NAME)
        local_file_path = metadata_path.replace(metadata_folder_prefix, "")
        local_file_path = local_file_path.rsplit(".cnvrg", 1)[0]  # Remove the extension of the metadata file
        local_file_path = os.path.normpath(local_file_path)  # Normalize path to prevent double slashes if exists

        # Remove leading / is exists, so that the path won't be considered as absolute
        if local_file_path[0] == "/":
            local_file_path = local_file_path[1:]

        return local_file_path
