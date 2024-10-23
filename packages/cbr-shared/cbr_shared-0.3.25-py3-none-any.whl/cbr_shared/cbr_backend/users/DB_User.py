import re
from cbr_shared.aws.s3.S3_DB_Base                               import S3_DB_Base
from cbr_shared.schemas.data_models.Model__Chat__Saved          import Model__Chat__Saved
from cbr_shared.schemas.data_models.Model__User__Config_Data    import Model__User__Config_Data
from cbr_shared.schemas.data_models.Model__User__Profile_Data   import Model__User__Profile_Data
from osbot_utils.helpers.Random_Guid                            import Random_Guid
from osbot_utils.utils.Http                                     import url_join_safe
from osbot_utils.utils.Status                                   import status_ok

S3_DB_User__BUCKET_NAME__SUFFIX = "db-users"                       # todo: change this name 'db-users' to something more relevant to S3_DB_Base (since this is a legacy name from the early statges of cbr dev)
S3_DB_User__BUCKET_NAME__PREFIX = 'cyber-boardroom'

FILE_NAME__USER__CONFIG         = 'user-config.json'
FILE_NAME__USER__PROFILE        = 'user-profile.json'
FILE_NAME__USER__PAST_CHATS     = 'user-past-chats.json'

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

    def create(self, user_config: Model__User__Config_Data = None,  user_profile:Model__User__Profile_Data = None):
        if user_config is None:
            user_config = Model__User__Config_Data.random_user()
        if user_profile is None:
            user_profile = Model__User__Profile_Data()

        self.user_config__update (user_config)
        self.user_profile__update(user_profile)
        return status_ok()


    def delete(self):
        s3_key_user_files = [self.s3_key_user__config    (),
                             self.s3_key_user__past_chats(),
                             self.s3_key_user__profile   ()]
        self.s3_files_delete(s3_key_user_files)
        return self.s3_folder_user_data__files() == []                  # this will confirm that everything has been deleted

    def exists(self):
        return self.s3_file_exists(self.s3_key_user__profile())

    def not_exists(self):
        return self.exists() is False

    def user_config__update(self, user_config: Model__User__Config_Data):
        if type(user_config) is Model__User__Config_Data:
            return self.s3_save_data(data=user_config.json(), s3_key=self.s3_key_user__config())
        raise ValueError("user_config_data needs to be of type Model__User__Config_Data")

    def user_profile__update(self, user_profile: Model__User__Profile_Data):
        if type(user_profile) is Model__User__Profile_Data:
            return self.s3_save_data(data=user_profile.json(), s3_key=self.s3_key_user__profile())
        raise ValueError("user_profile_data needs to be of type Model__User__Profile_Data")



    # s3 folders and keys
    def s3_folder_user_data(self):
        return self.user_id

    def s3_folder_user_data__files(self):
        return self.s3_folder_files(self.s3_folder_user_data())

    def s3_key_in_user_folder(self, file_name):
        return url_join_safe(self.s3_folder_user_data(), file_name)

    def s3_key_user__config(self):
        return self.s3_key_in_user_folder(FILE_NAME__USER__CONFIG)

    def s3_key_user__profile(self):
        return self.s3_key_in_user_folder(FILE_NAME__USER__PROFILE)

    def s3_key_user__past_chats(self):
        return self.s3_key_in_user_folder(FILE_NAME__USER__PAST_CHATS)


    # user data related methods

    def user_past_chats(self):
        s3_key_past_chats = self.s3_key_user__past_chats()
        if self.s3_file_exists(s3_key_past_chats):
            return self.s3_file_contents_json(s3_key_past_chats)
        return {}

    def user_past_chats__clear(self):
        return self.s3_save_data({}, self.s3_key_user__past_chats())

    def user_past_chats__add_chat(self, chat_path):
        safe_chat_path = re.sub(r'[^0-9a-f\-/]', '', chat_path)     # refactor to central location with these regexes
        if safe_chat_path != chat_path:
            return False
        past_chats = self.user_past_chats()
        if 'saved_chats' not in past_chats:
            past_chats['saved_chats'] = {}
        new_chat = Model__Chat__Saved(chat_path=safe_chat_path, user_id=self.user_id)
        past_chats['saved_chats'][new_chat.chat_id] = new_chat.json()
        if self.s3_save_data(past_chats, self.s3_key_user__past_chats()):
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

    def user_config(self) -> Model__User__Config_Data:
        s3_key_user_config = self.s3_key_user__config()
        if self.s3_file_exists(s3_key_user_config):
            user_config_json = self.s3_file_contents_json(s3_key_user_config)
            user_config      = Model__User__Config_Data(**user_config_json)
            return user_config
        return None

    def user_data(self):
        return { 'config'    : self.user_config     ().json(),
                 'past_chats': self.user_past_chats ()       ,
                 'profile'   : self.user_profile    ().json()}

    def user_profile(self) -> Model__User__Profile_Data:
        s3_key_user_profile = self.s3_key_user__profile()
        if self.s3_file_exists(s3_key_user_profile):
            user_profile_json = self.s3_file_contents_json(s3_key_user_profile)
            user_profile      = Model__User__Profile_Data.from_json(user_profile_json)
            return user_profile
        return None