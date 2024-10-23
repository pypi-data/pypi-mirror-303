from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.utils.Misc import random_text


class CBR__Service_Accounts(Type_Safe):
    service_accounts: dict

    def add_service_account(self, session_id: str, account_data: dict):
        self.service_accounts[session_id] = account_data

    def get_service_account(self, session_id: str) -> dict:
        return self.service_accounts.get(session_id, {})


    def create_service_account__empty_session(self, **kwargs):
        random_session_id   = random_text('session_id')
        random_session_data = dict(an_random_value=random_text('session_data'), **kwargs)
        self.add_service_account(random_session_id, random_session_data)
        return random_session_id, random_session_data

    def create_service_account__admin_session(self):
        session_data = {'username': random_text('an_admin'), 'cognito:groups': ['CBR-Team']}
        user_data    = dict()
        kwargs       = dict(session_data=session_data, user_data=user_data)
        return self.create_service_account__empty_session(**kwargs)