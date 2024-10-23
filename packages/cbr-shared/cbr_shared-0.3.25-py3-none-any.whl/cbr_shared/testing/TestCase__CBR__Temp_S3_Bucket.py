from unittest                                            import TestCase
from cbr_shared.cbr_backend.cbr.S3_DB__CBR               import S3_DB__CBR
from osbot_aws.AWS_Config                                import aws_config
from osbot_utils.utils.Misc                              import random_text


class TestCase__CBR__Temp_S3_Bucket(TestCase):

    @classmethod
    def setUpClass(cls):
        bucket_suffix  = random_text('suffix', lowercase=True).replace('_','-')
        bucket_prefix  = random_text('prefix', lowercase=True).replace('_','-')
        cls.s3_db_cbr  = S3_DB__CBR(bucket_name__suffix=bucket_suffix, bucket_name__prefix=bucket_prefix)
        with cls.s3_db_cbr as _:
            assert _.using_local_stack() is True                      # confirm we are using Minio
            _.setup()                                                 # this will create the temp bucket
            assert _.bucket_exists() is True
            assert _.s3_bucket() == f'{bucket_prefix}-{aws_config.account_id()}-{bucket_suffix}'

    @classmethod
    def tearDownClass(cls):
        with cls.s3_db_cbr as _:
            assert _.bucket_delete_all_files() is True
            assert _.bucket_delete          () is True