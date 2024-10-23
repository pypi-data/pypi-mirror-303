import cbr_content

import cbr_shared
from cbr_shared.demo.Demo__User             import Demo__User
from osbot_utils.base_classes.Type_Safe     import Type_Safe
from osbot_utils.utils.Files                import path_combine
from osbot_utils.utils.Misc                 import list_set
from osbot_utils.utils.Toml                 import toml_dict_from_file

FILE_NAME___DEMO_USERS__CONFIG_FILE = 'en/web-site/demo-users/users.toml'

# todo: change this to use the new Guest features
class Demo_Users(Type_Safe):

    def demo_user(self, user_name):
        user_data  = self.users_data().get(user_name)
        if user_data:
            return Demo__User.from_json(user_data)
        raise ValueError(f'Demo user with name `{user_name}` not found')

    def path_config_file(self):
        return path_combine(cbr_content.path,FILE_NAME___DEMO_USERS__CONFIG_FILE)

    def users_data(self):
        return  toml_dict_from_file(self.path_config_file())

    def users_names(self):
        return list_set(self.users_data())
