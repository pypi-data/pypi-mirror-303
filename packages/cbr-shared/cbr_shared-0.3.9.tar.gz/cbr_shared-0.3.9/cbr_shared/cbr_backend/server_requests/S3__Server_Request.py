from cbr_shared.cbr_backend.server_requests.S3_DB__Server_Requests   import S3_DB__Server_Requests
from osbot_fast_api.api.Fast_API__Http_Event                         import Fast_API__Http_Event
from osbot_utils.base_classes.Type_Safe                              import Type_Safe
from osbot_utils.context_managers.capture_duration import capture_duration
from osbot_utils.helpers.Random_Guid                                 import Random_Guid
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Files import parent_folder
from osbot_utils.utils.Misc                                          import timestamp_to_str_time


class S3__Server_Request(Type_Safe):
    s3_db        : S3_DB__Server_Requests
    when         : str                      = None
    event_id     : Random_Guid
    request_data : Fast_API__Http_Event   = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.request_data:
            self.event_id = self.request_data.event_id

    def create(self):
        with capture_duration(action_name='save-to-s3') as duration:
            result =  (self.create__event_data         () and
                       self.create__http_event_info    () and
                       self.create__http_event_request () and
                       self.create__http_event_response() and
                       self.create__http_event_traces  ()    )

            #self.request_data.create_duration = duration                   # todo: figure out a better place to log this
            self.create__event_data()
            return result

    def create__event_data(self):
        if self.request_data:
            s3_key    = self.s3_key()
            data      = self.request_data.json()
            metadata  = dict(s3_key       = s3_key                                                           ,
                             request_path = self.request_data.http_event_request.path                        ,
                             status_code  = str(self.request_data.http_event_response.status_code            ),
                             timestamp    = str(self.request_data.http_event_info.timestamp                  ),
                             time         = timestamp_to_str_time(self.request_data.http_event_info.timestamp),
                             duration     = str(self.request_data.http_event_request.duration                ),
                             content_size = str(self.request_data.http_event_response.content_length         ),
                             method       = self.request_data.http_event_request.method                      )
            return self.s3_db.s3_save_data(data=data, s3_key=s3_key, metadata=metadata)

    def create__http_event_info(self):
        return self.create__from_request_data_field_name('http_event_info')

    def create__http_event_request(self):
        return self.create__from_request_data_field_name('http_event_request')

    def create__http_event_response(self):
        return self.create__from_request_data_field_name('http_event_response')

    def create__http_event_traces(self):
        return self.create__from_request_data_field_name('http_event_traces')

    def create__from_request_data_field_name(self,field_name):
        data = getattr(self.request_data, field_name)
        data_json = data.json()
        s3_key = self.s3_key(field_name)
        return self.s3_db.s3_save_data(data=data_json, s3_key=s3_key)

    def create_from_request_data(self, request_data: Fast_API__Http_Event):
        self.request_data = request_data
        self.event_id     = request_data.event_id
        return self.create()

    def delete(self):
        return self.s3_db.s3_file_delete(self.s3_key())

    def exists(self):
        return self.s3_db.s3_file_exists(self.s3_key())

    def metadata(self):
        return self.s3_db.s3_file_metadata(self.s3_key())

    def load(self, s3_key):
        raw_data          = self.s3_db.s3_file_data(s3_key)       # we can't use self.s3_key()  since there are scenarios where data from request_data is needed
        if raw_data:
            self.request_data = Fast_API__Http_Event.from_json(raw_data)
            self.event_id     = self.request_data.event_id
        return self


    def s3_key(self, file_type=None):
        if file_type is None:
            file_type = 'http_event'
        kwargs = dict(when         = self.when          ,
                      event_id     = self.event_id      ,
                      request_path = self.request_path(),
                      file_type    = file_type          )
        return self.s3_db.s3_key(**kwargs)

    def s3_key_folder(self):
        return parent_folder(self.s3_key())

    def request_path(self):
        if self.request_data:
            return self.request_data.http_event_request.path


