from cbr_shared.aws.s3.S3__Key_Generator import S3__Key_Generator
from osbot_utils.utils.Misc              import random_guid

VALUE__REQUEST_TYPE__UNKNOWN = 'unknown'

class S3__Key__Servers(S3__Key_Generator):
    use_request_path  : bool = False

    def create__for__server(self, server_id=None, event_type=None, event_id=None):
        path_elements = self.create_path_elements__from_when()

        if not server_id   : server_id    = random_guid()
        if not event_id    : event_id     = random_guid()
        if not event_type  : event_type   = VALUE__REQUEST_TYPE__UNKNOWN

        path_elements.append(server_id)
        path_elements.append(event_type)

        file_id = event_id

        s3_key = self.create_s3_key(path_elements=path_elements, file_id=file_id)
        return s3_key

