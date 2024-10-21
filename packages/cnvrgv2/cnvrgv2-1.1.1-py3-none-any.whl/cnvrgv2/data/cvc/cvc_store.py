import os
import shutil
import time

import requests

from cnvrgv2.config import Config, CONFIG_FOLDER_NAME
from cnvrgv2.config.error_messages import CONFIG_YAML_NOT_FOUND
from cnvrgv2.data.cvc.cvc_metadata import CvcMetadata
from cnvrgv2.data.cvc.data_transfers.cvc_downloader import CvcDownloader
from cnvrgv2.data.cvc.data_transfers.cvc_put_files import CvcPutFiles
from cnvrgv2.data.cvc.data_transfers.cvc_simple_store_cloner import CvcSimpleStoreCloner
from cnvrgv2.data.cvc.data_transfers.cvc_simple_uploader import CvcSimpleUploader
from cnvrgv2.data.cvc.data_transfers.cvc_store_cloner import CvcStoreCloner
from cnvrgv2.data.cvc.data_transfers.cvc_uploader import CvcUploader
from cnvrgv2.data.cvc.error_messages import CVC_COMMIT_IS_NOT_THE_LATEST, CVC_DATA_OWNER_OBJECT_CONFIG_CONFLICT, \
    CVC_DOWNLOAD_LATEST_COMMIT, CVC_STORE_ALREADY_CLONED
from cnvrgv2.data.cvc.errors import CvcStoreAlreadyClonedError
from cnvrgv2.data.cvc.routes import CVC_COMMIT_BASE, CVC_COMMITS_BASE, CVC_STORE_BASE
from cnvrgv2.errors import CnvrgCommitError, CnvrgError, CnvrgFileError, CnvrgHttpError
from cnvrgv2.proxy import HTTP
from cnvrgv2.utils.json_api_format import JAF


class CvcStore:
    TMP_FOLDER_NAME = ".tmp"

    def __init__(self, proxy, storage_client, attributes):
        """
        Constructor for the cvc service
        @param cvc_base_url: Base url of the cvc service
        @param cnvrg_dataset: A cnvrg dataset object. Used to get storage credentials
        """
        self.proxy = proxy
        # TODO: The following lines is a patch for phase1 and needs to be reorganized in phase 2
        self.storage_client = storage_client
        self.slug = attributes["slug"]
        self._attributes = attributes
        self.route = CVC_STORE_BASE.format(self.slug)
        self.config = Config()

    @property
    def _working_dir(self):
        """
        The working dir for this store. It needs to be calculated at each call, so that the value will be the correct
        one, in case the user created the CvcStore in dir x, moved to dir y and called a function of CvcStore
        that uses the _working_dir (like clone).
        @return: The working dir for this store.
        """
        return os.path.join(os.getcwd(), self.slug)

    def cvc_clone(self, commit_sha1='latest', threads=40):
        """
        Clones the store into a new folder with the name of the store's slug.
        @param commit_sha1: String. The commit to clone
        @param threads: Integer. Number of threads to use for the download process
        @return: None
        """
        # TODO: In production change to reload
        self.config = Config()

        commit_to_clone = commit_sha1
        local_config_path = os.path.join(self._working_dir, CONFIG_FOLDER_NAME)
        old_wording_dir = os.getcwd()

        try:
            self._prepare_directory_before_clone()
            os.chdir(self.slug)

            # If latest, fetch the commit_sha1
            if commit_to_clone == "latest":
                commit_to_clone = self._get_commit(commit_sha1=commit_to_clone).get("sha1")

                if not commit_to_clone:
                    # No commit in store yet. Just create the config and exit
                    self.save_config(self.slug, commit_to_clone, local_config_path=local_config_path)
                    return

            downloader = CvcStoreCloner(self, commit_to_clone, num_workers=threads)

            while downloader.in_progress:
                time.sleep(1)

            if downloader.errors:
                if os.path.exists(self.slug):
                    shutil.rmtree(self.slug)
                raise CnvrgError(downloader.errors.args)

            self.save_config(self.slug, commit_to_clone, local_config_path=local_config_path)

        except CvcStoreAlreadyClonedError:
            return
        finally:
            os.chdir(old_wording_dir)

    def cvc_simple_clone(self, commit_sha1='latest', threads=40):
        """
        Clones the store into a new folder with the name of the store's slug.
        @param commit_sha1: String. The commit to clone
        @param threads: Integer. Number of threads to use for the download process
        @return: None
        """
        # TODO: In production change to reload
        self.config = Config()

        commit_to_clone = commit_sha1
        local_config_path = os.path.join(self._working_dir, CONFIG_FOLDER_NAME)

        try:
            self._prepare_directory_before_clone()

            # If latest, fetch the commit_sha1
            if commit_to_clone == "latest":
                commit_to_clone = self._get_commit(commit_sha1=commit_to_clone).get("sha1")

                if not commit_to_clone:
                    # No commit in store yet. Just create the config and exit
                    self.save_config(self.slug, commit_to_clone, local_config_path=local_config_path)
                    return

            cloner = CvcSimpleStoreCloner(self, commit_sha1=commit_to_clone, num_workers=threads)
            cloner.download()

            self.save_config(self.slug, commit_to_clone, local_config_path=local_config_path)

        except CvcStoreAlreadyClonedError:
            return

    def cvc_upload(self):
        """
        Uploads the changes in the current directory. The directory must be a cloned project or dataset
        @return: None
        """
        # TODO: In production change to reload
        self.config = Config()

        self._upload_verifications()
        current_commit_sha1 = self.config.commit_sha1
        new_commit_sha1 = self._create_new_commit(current_commit_sha1)["sha1"]
        uploader = CvcUploader(self, new_commit_sha1, [self.config.root])

        while uploader.in_progress:
            time.sleep(0.1)

        # TODO: Decide on error behaviour later
        if uploader.errors:
            raise uploader.errors[0]

        self.save_config(self.slug, new_commit_sha1)

    def cvc_put_files(self, paths):
        """
        Uploads given files to the latest commit
        @return: None
        """
        paths_to_upload = paths if isinstance(paths, list) else [paths]

        new_commit_sha1 = self._create_new_commit(parent_commit=None, copy_previous_commit=True)["sha1"]
        uploader = CvcPutFiles(self, new_commit_sha1, paths_to_upload)

        while uploader.in_progress:
            time.sleep(0.1)

        # TODO: Decide on error behaviour later
        if uploader.errors:
            raise uploader.errors[0]

    def cvc_upload_simple(self):
        """
        Uploads the changes in the current directory. The directory must be a cloned project or dataset
        @return: None
        """
        # TODO: In production change to reload
        self.config = Config()

        self._upload_verifications()
        current_commit_sha1 = self.config.commit_sha1
        new_commit_sha1 = self._create_new_commit(current_commit_sha1)["sha1"]
        uploader = CvcSimpleUploader(store=self, commit_sha1=new_commit_sha1, paths=[self.config.root])
        uploader.upload()
        self.save_config(self.slug, new_commit_sha1)

    def cvc_download(self):
        """
        Downloads the changes from latest commit to the current directory.
         The directory must be a cloned project or dataset.
        @return: None
        """
        # TODO: In production change to reload
        try:
            self.config = Config()
            latest_commit = self._download_verifications()
            downloader = CvcDownloader(self, latest_commit)

            while downloader.in_progress:
                time.sleep(0.1)

            # TODO: Decide on error behaviour later
            if downloader.errors:
                raise downloader.errors[0]

            # TODO file deleter

            self.save_config(self.slug, latest_commit)
        except CnvrgCommitError:
            return

    def _upload_verifications(self):
        # TODO: In production refactor to _validate_config_ownership (part of data_owner)
        #   But keep all three validations
        if not self.config.dataset_slug and not self.config.project_slug:
            raise CnvrgFileError(CONFIG_YAML_NOT_FOUND)
        elif self.slug not in [self.config.dataset_slug, self.config.project_slug]:
            raise CnvrgFileError(CVC_DATA_OWNER_OBJECT_CONFIG_CONFLICT)
        elif self.config.commit_sha1 != self._get_commit().get("sha1"):
            raise CnvrgFileError(CVC_COMMIT_IS_NOT_THE_LATEST)

    def _download_verifications(self):
        # TODO: In production refactor to _validate_config_ownership (part of data_owner)
        #   But keep all three validations
        if not self.config.dataset_slug and not self.config.project_slug:
            raise CnvrgFileError(CONFIG_YAML_NOT_FOUND)
        elif self.slug not in [self.config.dataset_slug, self.config.project_slug]:
            raise CnvrgFileError(CVC_DATA_OWNER_OBJECT_CONFIG_CONFLICT)
        latest_commit = self._get_commit().get("sha1")
        current_commit_sha1 = self.config.commit_sha1
        if current_commit_sha1 == latest_commit:
            raise CnvrgCommitError(CVC_DOWNLOAD_LATEST_COMMIT)
        # return the latest commit to spare another api call, not sure if it's necessary
        return latest_commit

    def _prepare_directory_before_clone(self):
        if not os.path.exists(self._working_dir):
            # Creates the store folder and the metadata folder
            os.makedirs(os.path.join(self._working_dir, CONFIG_FOLDER_NAME, CvcMetadata.METADATA_FOLDER_NAME))
        elif os.path.exists(self._working_dir + '/' + CONFIG_FOLDER_NAME):
            raise CvcStoreAlreadyClonedError(CVC_STORE_ALREADY_CLONED)

    def save_config(self, slug, commit_sha1, local_config_path=None):
        """
        Saves info on the config file
        @param slug: String. Slug of the store
        @param commit_sha1: String. The currently cloned commit
        @param local_config_path: String. Override the local config path -
                                can be used to create new cnvrg project or dataset
        @return: None
        """
        # TODO: In production, the config should have more fields
        #   Also we shouldn't save dataset and project slug. MUST BE REFACTORED BEFORE PRODUCTION
        self.config.update(local_config_path=local_config_path, **{
            "dataset_slug": slug,
            "project_slug": slug,
            "commit_sha1": commit_sha1
        })

    def _get_commit(self, commit_sha1="latest"):
        """
        Fetches a commit
        @param commit_sha1: String. Sha1 of the commit
        @return: Dictionary containing commits attributes
        """
        # TODO: In production consider moving this function to it's own class (Commit.py) or other elegant solution
        try:
            response = self.proxy.call_api(
                route=CVC_COMMIT_BASE.format(self.slug, commit_sha1),
                http_method=HTTP.GET
            )
            return response.attributes
        except CnvrgHttpError as e:
            # TODO: Remove the 500 handling after bug fix
            if e.status_code in [requests.codes.not_found, requests.codes.server_error]:
                return {}
            raise e

    def _create_new_commit(self, parent_commit, copy_previous_commit=False):
        """
        Creates a new commit
        @param parent_commit: String. The former commit in the chain
        @return: Dictionary containing commits attributes
        """
        attributes = {
                "parent": parent_commit
        }
        if copy_previous_commit:
            attributes['copy_previous_commit'] = True

        response = self.proxy.call_api(
            route=CVC_COMMITS_BASE.format(self.slug),
            http_method=HTTP.POST,
            payload=JAF.serialize(type="cvc", attributes=attributes)
        )
        return response.attributes
