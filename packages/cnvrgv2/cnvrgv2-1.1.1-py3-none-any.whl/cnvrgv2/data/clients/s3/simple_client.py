import boto3
import botocore
from boto3.s3.transfer import TransferConfig

from cnvrgv2.data.clients.base_storage_client import BaseStorageClient
from cnvrgv2.utils.retry import retry
from cnvrgv2.utils.storage_utils import create_dir_if_not_exists

config = TransferConfig(max_concurrency=10, use_threads=True)


class S3SimpleStorage(BaseStorageClient):
    def __init__(self, storage_meta):
        super().__init__(storage_meta)

        props = self._decrypt_dict(storage_meta, keys=["sts_a", "sts_s", "sts_st", "bucket", "region"])
        print("decrypted: {}".format(props.get("sts_st")))
        self.s3props = {
            "aws_access_key_id": "ASIAR3BPBD2NNRPETKFB",
            "aws_session_token": "IQoJb3JpZ2luX2VjEKP//////////wEaCXVzLWVhc3QtMiJIMEYCIQDjB7ZVmwS5EsP9ZRkaHeLoFKSibACld"
                                 "vgKOmX0/nvDyAIhANLsgplPN5ym6gBarXZj2EtF4cy0Dqutv1D8zyphGCNUKqICCCwQAxoMMTI2ODAwMTc"
                                 "0NzQ2Igwn8tPJRw4Ze1CpJnwq/wHWO4MqIvvwLLB24b5Gb9UztwO3vWaQA867ndMnQSjgn5TsHwpWk9H"
                                 "omFQs4jbQaB6ijvOYsZpNQ75rcEvzZOL9rdIMN7dBj/vuTJkCKaMOtNtoh2psvozCcJfhDvLF8cs0t++"
                                 "Dfkv2V2TkF+JN3DqvBvXjflTIcUJljz4+AmfBMPopC7TPqS1dWyzn3HJ5Jxw7yCyyMC2Kh9pWCugez/nhM"
                                 "Jt/XLOvYmgPJA074iLzmkTup0hKa2WX9qUY5QGAOxZY3RHIVi/Ntw6vOZw7P3J3VJd+irPo7YTrSXtbu3Ph"
                                 "iNKFjCTvx4cq2tIu6KRxRo7OecK1XY1f1rDgL1xoNacwxZ/+ngY6nAFbJH7K9JOoEL7FfvJdirfaKah"
                                 "LO3szHUfUOJVch2+ryRShE3RH0ZA88dTfDvUHtkeCCDUAVzqaLx1DUM7q4xcTMwaDBjJ5d4CPUVWLt76"
                                 "3CUlhsc3jhCV9BZVqMlPQ3rMzNuKQ47w86USD5X6CEOU/YKKKgW6BIuN9b4c2QQcP3ZLk/3chFHR44u"
                                 "AUGPKOtO/LrpXAfbMVF0HfW3U=",
            "aws_secret_access_key": "KvXHEKl4iSaZQYgW4rymNyPvyM3vQ3Ti6VUdOY5/",
            "region_name": props.get("region")
        }
        self.bucket = props.get("bucket")
        self.region = props.get("region")
        self.client = self._get_client()
        self.sum = 0

    @retry(log_error=True)
    def upload_single_file(self, local_path, object_path, progress_bar=None):
        try:
            self.client.upload_file(
                local_path,
                self.bucket,
                object_path,
                Config=config,
                Callback=self.progress_callback(progress_bar)
            )
        except Exception as e:
            print(e)

    @retry(log_error=True)
    def download_single_file(self, local_path, object_path, progress_bar=None):
        try:
            create_dir_if_not_exists(local_path)
            if not object_path:
                return

            self.client.download_file(
                self.bucket,
                object_path,
                local_path,
                Config=config,
                Callback=self.progress_callback(progress_bar)
            )
        except Exception as e:
            raise e

    def _get_client(self):
        botocore_config = botocore.config.Config(max_pool_connections=50)
        return boto3.client('s3', config=botocore_config, **self.s3props, verify=self.check_certificate)
