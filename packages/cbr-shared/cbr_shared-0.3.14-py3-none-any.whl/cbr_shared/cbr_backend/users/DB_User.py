import re

from botocore.exceptions                                import ClientError
from cbr_shared.aws.s3.S3_DB_Base                       import S3_DB_Base
from cbr_shared.schemas.data_models.Model__Chat__Saved  import Model__Chat__Saved
from osbot_utils.helpers.Random_Guid                    import Random_Guid
from osbot_utils.utils.Http                             import url_join_safe
from osbot_utils.utils.Json                             import json_dumps, json_loads

S3_DB_User__BUCKET_NAME__SUFFIX = "db-users"                       # todo: change this name 'db-users' to something more relevant to S3_DB_Base (since this is a legacy name from the early statges of cbr dev)
S3_DB_User__BUCKET_NAME__PREFIX = 'cyber-boardroom'

FILE_NAME__USER__METADATA       = 'metadata.json'
FILE_NAME__USER__PAST_CHATS     = 'past_chats.json'

class DB_User(S3_DB_Base):
    bucket_name__suffix: str         = S3_DB_User__BUCKET_NAME__SUFFIX
    bucket_name__prefix: str         = S3_DB_User__BUCKET_NAME__PREFIX
    user_id            : Random_Guid

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.user_id is None:
            self.user_id = Random_Guid()

    def __enter__(self                        ): return self
    def __exit__ (self, type, value, traceback): pass
    def __repr__ (self                        ): return f"<DB_User: {self.user_id}>"

    def create(self):
        metadata_as_str = json_dumps(self.default_metadata())
        kwargs = dict(file_contents = metadata_as_str,
                      bucket        = self.s3_bucket(),
                      key           = self.s3_key_user_metadata())
        return self.s3().file_create_from_string(**kwargs)

    def delete(self):
        kwargs = dict(bucket        = self.s3_bucket(),
                      key           = self.s3_key_user_metadata())
        return self.s3().file_delete(**kwargs)

    def exists(self):
        return self.s3().file_exists(self.s3_bucket(), self.s3_key_user_metadata())

    def metadata(self):
        try:
            raw_data = self.s3().file_contents(self.s3_bucket(), self.s3_key_user_metadata())
            return json_loads(raw_data)
        except ClientError:
            return {}

    def metadata_update(self, metadata):
        metadata_as_str = json_dumps(metadata)
        kwargs = dict(file_contents = metadata_as_str,
                      bucket        = self.s3_bucket(),
                      key           = self.s3_key_user_metadata())
        return self.s3().file_create_from_string(**kwargs)


    def default_metadata(self):
        return { 'user_id': self.user_id ,
                 'type'   : 'pytest_user'}

    # def s3_folder_user_profile(self, user_id):
    #     return f'{self.s3_folder_user_profiles()}/{user_id}'

    def get_metadata_value(self, key):
        return self.metadata().get(key)

    def s3_folder_user_data(self):
        return self.user_id

    def s3_key_user_metadata(self):
        return f'{self.s3_folder_user_data()}/{FILE_NAME__USER__METADATA}'

    def s3_key_user_past_chats(self):
        return f'{self.s3_folder_user_data()}/{FILE_NAME__USER__PAST_CHATS}'

    def set_metadata_value(self, key,value):
        metadata = self.metadata()
        metadata[key] = value
        return self.metadata_update(metadata)

    def set_metadata_values(self, values):
        metadata = self.metadata()
        for key,value in values.items():
            metadata[key] = value
        return self.metadata_update(metadata)

    # user data related methods

    def user_past_chats(self):
        s3_key_past_chats = self.s3_key_user_past_chats()
        if self.s3_file_exists(s3_key_past_chats):
            return self.s3_file_contents_json(s3_key_past_chats)
        return {}

    def user_past_chats__clear(self):
        return self.s3_save_data({}, self.s3_key_user_past_chats())

    def user_past_chats__add_chat(self, chat_path):
        safe_chat_path = re.sub(r'[^0-9a-f\-/]', '', chat_path)     # refactor to central location with these regexes
        if safe_chat_path != chat_path:
            return False
        past_chats = self.user_past_chats()
        if 'saved_chats' not in past_chats:
            past_chats['saved_chats'] = {}
        new_chat = Model__Chat__Saved(chat_path=safe_chat_path, user_id=self.user_id)
        past_chats['saved_chats'][new_chat.chat_id] = new_chat.json()
        if self.s3_save_data(past_chats, self.s3_key_user_past_chats()):
            return new_chat

    def user_past_chats__in_table(self):
        headers = ['chat_id', 'view', 'user_id']
        rows = []
        chats = self.user_past_chats()
        if chats:
            for chat_id, chat_raw in chats.get('saved_chats').items():
                chat = Model__Chat__Saved.from_json(chat_raw)
                row = []
                row.append(chat.chat_id)
                row.append(f"""<a href='chat/view/{chat.chat_path}'      target="_blank">web page</a> |  
                               <a href='chat/view/{chat.chat_path}/pdf'   target="_blank">pdf</a> |  
                               <a href='chat/view/{chat.chat_path}/image' target="_blank">image</a>""")
                row.append(chat.user_id)

                rows.append(row)

        return dict(headers=headers, rows=rows)

    def user_profile(self):
        metadata = self.metadata()
        if metadata:
            if 'cognito_data' in metadata:
                del metadata['cognito_data']
            return metadata
        return {}