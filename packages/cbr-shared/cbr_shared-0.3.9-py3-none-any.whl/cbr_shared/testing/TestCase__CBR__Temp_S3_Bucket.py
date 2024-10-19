from unittest import TestCase

from cbr_shared.aws.s3.S3_DB_Base                    import ENV_NAME__USE_MINIO_AS_S3
from cbr_shared.cbr_backend.cbr.S3_DB__CBR import S3_DB__CBR
from osbot_aws.testing.Temp__Random__AWS_Credentials import Temp__Random__AWS_Credentials
from osbot_utils.utils.Env import get_env


class TestCase__CBR__Temp_S3_Bucket(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.extra_env_vars   = { ENV_NAME__USE_MINIO_AS_S3: 'True'}
        cls.random_aws_creds = Temp__Random__AWS_Credentials(env_vars=cls.extra_env_vars).set_vars()
        assert get_env(ENV_NAME__USE_MINIO_AS_S3) == 'True'                                          # confirm value has been set
        cls.s3_db_cbr        = S3_DB__CBR(use_minio=True)
        with cls.s3_db_cbr as _:
            assert _.using_minio() is True                      # confirm we are using Minio
            _.setup()                                           # this will create the temp bucket
            assert _.bucket_exists() is True

    @classmethod
    def tearDownClass(cls):
        with cls.s3_db_cbr as _:
            assert _.bucket_delete_all_files() is True
            assert _.bucket_delete          () is True
        cls.random_aws_creds.restore_vars()