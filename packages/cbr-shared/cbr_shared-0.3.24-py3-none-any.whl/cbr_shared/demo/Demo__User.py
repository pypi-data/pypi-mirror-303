from cbr_shared.cbr_backend.session.DB_Session  import DB_Session
from cbr_shared.cbr_backend.users.DB_User       import DB_User
from osbot_utils.base_classes.Type_Safe         import Type_Safe
from osbot_utils.helpers.Random_Guid            import Random_Guid


class Demo__User(Type_Safe):
    user_id    : Random_Guid
    session_id : str
    user_name  : str
    first_name : str
    last_name  : str

    def db_user(self):
        return DB_User(user_id=self.user_id)

    def db_session(self):
        return DB_Session(session_id=self.session_id)

    def setup(self):
        if self.db_user().exists() is False:

            return 'User not found'