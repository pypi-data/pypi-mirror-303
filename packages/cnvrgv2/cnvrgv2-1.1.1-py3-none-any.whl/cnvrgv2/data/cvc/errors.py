from cnvrgv2.errors import CnvrgError


class CvcStoreAlreadyClonedError(CnvrgError):
    def __init__(self, message):
        super(CnvrgError, self).__init__(message)


class CvcBadCommitError(CnvrgError):
    def __init__(self, message):
        super(CnvrgError, self).__init__(message)


class CvcMalfunctioningFilesCollector(CnvrgError):
    def __init__(self, message):
        super(CnvrgError, self).__init__(message)


class CvcChunkSizeExceeded(CnvrgError):
    def __init__(self, message):
        super(CnvrgError, self).__init__(message)
