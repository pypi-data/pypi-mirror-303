from cbr_shared.aws.s3.S3_DB_Base__Disabled                         import S3_DB_Base__Disabled
from cbr_shared.cbr_backend.server_requests.S3_DB__Server_Requests  import S3_DB__Server_Requests


class S3_DB__Server_Requests__Disabled(S3_DB__Server_Requests, S3_DB_Base__Disabled):

    def s3_key(self, **kwargs):
        return None

    def log_event(self, *args, **kwargs):
        import traceback

        return None