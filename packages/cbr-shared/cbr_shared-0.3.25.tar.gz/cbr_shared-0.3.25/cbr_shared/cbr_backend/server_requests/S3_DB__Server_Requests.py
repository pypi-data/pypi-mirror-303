from cbr_shared.cbr_backend.cbr.S3_DB__CBR                              import S3_DB__CBR
from cbr_shared.cbr_backend.server_requests.S3__Key__Server_Request     import S3__Key__Server_Request

S3_BUCKET_SUFFIX__SERVER_REQUESTS = 'server-requests'

class S3_DB__Server_Requests(S3_DB__CBR):
    bucket_name__suffix   : str = S3_BUCKET_SUFFIX__SERVER_REQUESTS
    save_as_gz            : bool = True
    s3_key_generator      : S3__Key__Server_Request


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.s3_key_generator as _:
            _.root_folder = S3_BUCKET_SUFFIX__SERVER_REQUESTS
            _.save_as_gz  = self.save_as_gz
            _.server_name = self.server_name

    def s3_key(self, **kwargs):
        s3_key = self.s3_key_generator.create(**kwargs)
        return s3_key
