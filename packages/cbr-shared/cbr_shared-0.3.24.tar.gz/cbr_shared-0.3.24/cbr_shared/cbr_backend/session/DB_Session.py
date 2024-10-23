from osbot_utils.utils.Http                 import url_join_safe
from cbr_shared.cbr_backend.cbr.S3_DB__CBR  import S3_DB__CBR
from osbot_utils.utils.Misc                 import timestamp_utc_now
from osbot_utils.utils.Str                  import str_safe

FILE_NAME_CURRENT_SESSION = 'session-data.json'

class DB_Session(S3_DB__CBR):

    def __init__(self, session_id):
        self.session_id  = str_safe(session_id)
        super().__init__()

    def __repr__ (self                        ): return f"<DB_Session: {self.session_id}>"

    def cbr_cookie(self):
        return f"CBR_TOKEN={self.session_id}"

    def create(self, data=None, metadata=None):
        session_data = self.create_session_data(data, metadata)
        s3_key       = self.s3_key__user_session()
        return self.s3_save_data(data=session_data, s3_key=s3_key)

    def create_session_data(self, data=None, metadata=None):
        session_data = { 'session_id' : self.session_id     ,
                         'timestamp'  : timestamp_utc_now() ,
                         'data'       : data or {}          }
        if metadata:
            session_data.update(metadata)
        return session_data

    def delete(self):
        s3_keys_to_delete = [self.s3_key__user_session()]
        self.s3_files_delete(s3_keys_to_delete)
        return self.s3_folder__user_session__files() == []                 # this will confirm that everything has been deleted

    def exists(self):
        return self.s3_file_exists(self.s3_key__user_session())

    def s3_folder__user_session(self):
        return url_join_safe(self.s3_folder_users_sessions(), self.session_id)

    def s3_folder__user_session__files(self):
        return self.s3_folder_files(self.s3_folder__user_session())

    def s3_key__user_session(self):
        return url_join_safe(self.s3_folder__user_session(), FILE_NAME_CURRENT_SESSION)

    def session_data(self, include_timestamp=True):
        if self.exists():
            session_data = self.s3_file_data(self.s3_key__user_session())
            if include_timestamp is False and 'timestamp' in session_data:
                del session_data['timestamp']
            return session_data
        return {}

    def source(self):
        return self.session_data().get('source')