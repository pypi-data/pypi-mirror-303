from unittest                                                       import TestCase
from cbr_shared.aws.s3.S3_DB_Base                                   import ENV_NAME__USE_MINIO_AS_S3
from cbr_shared.cbr_sites.CBR_Site__Shared_Objects                  import cbr_site_shared_objects
from cbr_shared.config.Server_Config__CBR_Website                   import server_config__cbr_website
from osbot_aws.testing.Temp__Random__AWS_Credentials                import Temp__Random__AWS_Credentials
from osbot_fast_api.utils.testing.Mock_Obj__Fast_API__Request_Data  import Mock_Obj__Fast_API__Request_Data


class TestCase__CBR__Temp_Servers(TestCase):                        # todo: refactor with deplicate code in the other TestCase__CBR__Temp_* classes

    @classmethod
    def setUpClass(cls):
        server_config__cbr_website.cbr_config().cbr_website.s3_log_requests    = True                               # enable s3_log_requests so that Minio works
        cls.extra_env_vars        = {ENV_NAME__USE_MINIO_AS_S3: 'True'}
        cls.random_aws_creds      = Temp__Random__AWS_Credentials(env_vars=cls.extra_env_vars).set_vars()
        cls.s3_db_servers         = cbr_site_shared_objects.s3_db_servers (reload_cache=True)
        cls.server_name           = server_config__cbr_website.server_name()
        with cls.s3_db_servers as _:
            assert _.using_minio() is True                      # confirm we are using Minio
            assert _.setup      () is _                         # this will create the temp bucket
            assert _.bucket_exists() is True



    @classmethod
    def tearDownClass(cls):
        with cls.s3_db_servers as _:
            assert _.using_minio() is True
            assert _.bucket_delete_all_files()
            assert _.bucket_delete() is True

        cls.random_aws_creds.restore_vars()
        server_config__cbr_website.cbr_config().cbr_website.s3_log_requests = False                 # restore back the s3_log_requests value (which should be false)
