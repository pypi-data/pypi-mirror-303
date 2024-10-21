CVC_STORE_CREATE_FAULTY_NAME = "Cannot create a cvc store with empty/non-string name."
CVC_STORE_GET_FAULTY_NAME = "Cannot get a cvc store with empty/non-string name."
CVC_STORE_ALREADY_CLONED = "The store {} is already cloned."
CVC_MALFUNCTION_IN_FILES_COLLECTOR = "File collector failed to function normally. There appears to be an " \
                                     "inconsistency between the file index and the total files. This may point to a " \
                                     "logical failure or a corrupt db representation of file chunks."

CVC_FAILED_TO_FETCH_CHUNK = "Failed to fetch chunk no {}, skipping. Error details {}"
CVC_RETRIES_EXCEEDED = "Exceeded number of download retries for {}, skipping."
CVC_GENERAL_DOWNLOAD_ERROR = "Unexpected error while downloading {}, skipping. Error details: {}"
CVC_DATA_OWNER_OBJECT_CONFIG_CONFLICT = "The used object represents a different data owner than the current folder."
CVC_COMMIT_IS_NOT_THE_LATEST = "Local commit is not the latest commit. Please download latest changes and try again."
CVC_METADATA_FILE_MISSING_KEY = "The {} key doesn't exist in the metadata file. Can't create object."
CVC_CHUNK_SIZE_EXCEEDED = "Can't send chunk to server. Chunk size must be up to {}."
CVC_BAD_COMMIT = "Commit doesn't exist."
CVC_EMPTY_STORE = "Store has no commits yet"

# DOWNLOAD
CVC_DOWNLOAD_LATEST_COMMIT = "The local commit is already aligned with latest commit, nothing to download"
