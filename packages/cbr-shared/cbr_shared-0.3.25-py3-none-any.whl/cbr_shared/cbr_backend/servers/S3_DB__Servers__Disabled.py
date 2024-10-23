from cbr_shared.aws.s3.S3_DB_Base__Disabled import S3_DB_Base__Disabled
from cbr_shared.cbr_backend.servers.S3_DB__Servers import S3_DB__Servers
from osbot_utils.utils.Status import status_warning


class S3_DB__Servers_Disabled(S3_DB__Servers, S3_DB_Base__Disabled):

    def s3_key(self, **kwargs):
        return None

    def log_event(self, *args, **kwargs):
        return status_warning("Warning: using S3_DB__Servers_Disabled, so no data will be saved.")

    def save_server_event(self, server_event):
        return status_warning("Warning: using S3_DB__Servers_Disabled, so no data will be saved.")