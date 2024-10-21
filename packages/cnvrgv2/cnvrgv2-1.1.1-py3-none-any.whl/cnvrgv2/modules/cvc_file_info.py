from pathlib import Path

from cnvrgv2.data.cvc.cvc_file import CvcFile
from cnvrgv2.modules.base.dynamic_attributes import DynamicAttributes


class CvcFileInfo(DynamicAttributes, CvcFile):
    available_attributes = {
        "file_name": str,
        "fullpath": str,
        "file_size": int,
        "created_at": str,
        "updated_at": str,
        "object_path": str
    }

    def __init__(self, context=None, slug=None, attributes=None):
        """
        This class represents cvc file info we want to expose to the user. Like in listing files.
        To avoid having two CvcFile classes, this class also inherits the CvcFile class used in the sdk inner logic
        @param context: Context object for this file
        @param slug: Identifier of this object. In this specific case, it's the file path.
        @param attributes: attributes of the file
        """
        self._context = context
        self._attributes = attributes or {}
        super(CvcFileInfo, self).__init__(local_path=slug, file_size=attributes.get("file_size", 0))

    @property
    def file_name(self):
        """
        Returns the file name extracted from the 'fullpath' attribute
        @return: list of the files' names
        """
        return Path(self.fullpath).name
