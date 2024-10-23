from cbr_shared.cbr_backend.cbr.S3_DB__CBR                  import S3_DB__CBR
from cbr_shared.cbr_backend.servers.S3__Key__Servers        import S3__Key__Servers
from cbr_shared.schemas.base_models.servers.Server_Event    import Server_Event
from osbot_utils.utils.Misc                                 import timestamp_utc_now, is_guid, timestamp_to_str_date, timestamp_to_str_time
from osbot_utils.utils.Status                               import status_ok, status_error

S3_BUCKET_SUFFIX__SERVERS    = 'servers'

class S3_DB__Servers(S3_DB__CBR):
    bucket_name__suffix   : str = S3_BUCKET_SUFFIX__SERVERS
    save_as_gz            : bool = True
    s3_key_generator      : S3__Key__Servers

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.s3_key_generator as _:
            _.root_folder      = S3_BUCKET_SUFFIX__SERVERS
            _.save_as_gz       = self.save_as_gz
            _.server_name      = self.server_name
            _.use_hours        = True
            _.use_minutes      = False
            _.use_request_path = False

    def s3_key(self, **kwargs):
        s3_key = self.s3_key_generator.create__for__server(**kwargs)
        return s3_key

    def log_event(self, **kwargs):
        server_event = Server_Event(**kwargs)
        return self.save_server_event(server_event)


    def save_server_event(self, server_event):
        if not server_event.timestamp:
            server_event.timestamp = timestamp_utc_now()

        event_id               = server_event.event_id
        event_message          = server_event.message
        event_type             = server_event.event_type
        level                  = server_event.level
        server_id              = server_event.server_id
        timestamp_date         = timestamp_to_str_date(server_event.timestamp)
        timestamp_time         = timestamp_to_str_time(server_event.timestamp)
        if is_guid(event_id) and is_guid(server_id):
            s3_key                 = self.s3_key(event_id=event_id, event_type=event_type, server_id=server_id)

            metadata               = { 'event_id'  : event_id       ,
                                       'message'   : event_message  ,
                                       'event_type': event_type     ,
                                       'server_id' : server_id      ,
                                       'date'      : timestamp_date ,
                                       'level'     : level          ,
                                       'time'      : timestamp_time }
            data = server_event.json()
            if self.s3_save_data(data=data, s3_key=s3_key, metadata=metadata):
                return status_ok(data={'file_data'    : data        ,
                                       'metadata'     : metadata    ,
                                       's3_key'       : s3_key      })
        return status_error(message="s3 save data failed")