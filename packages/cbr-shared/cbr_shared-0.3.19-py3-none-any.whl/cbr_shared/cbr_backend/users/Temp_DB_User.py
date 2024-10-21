from cbr_shared.cbr_backend.users.DB_Users import DB_Users
from osbot_utils.utils.Status import status_ok


class Temp_DB_User:

    def __init__(self):
        self.db_users = DB_Users()
        self.db_users.s3().dont_use_threads()
        self.db_user  = self.db_users.random_db_user()

    def __enter__(self):
        assert self.db_user.create() == status_ok()
        return self.db_user

    def __exit__(self, exc_type, exc_val, exc_tb):
        assert self.db_user.delete() is True
