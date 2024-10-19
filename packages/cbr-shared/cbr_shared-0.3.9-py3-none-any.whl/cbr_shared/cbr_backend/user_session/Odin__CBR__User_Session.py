from cbr_shared.cbr_backend.user_session.DyDB__CBR_User_Sessions import dydb_cbr_user_sessions
from cbr_shared.cbr_sites.CBR_Site__Shared_Objects      import cbr_site_shared_objects
from osbot_utils.base_classes.Type_Safe                 import Type_Safe
from osbot_utils.context_managers.capture_duration      import capture_duration
from osbot_utils.utils.Misc                             import to_int, timestamp_to_str_time, timestamp_to_str_date
from osbot_utils.utils.Status                           import status_error, status_ok


class Odin__CBR__User_Session(Type_Safe):

    def get_service_account_data(self, session_id):
        with cbr_site_shared_objects.cbr_service_accounts() as _:
            return _.get_service_account(session_id)

    def raw_user_session_data(self, session_id):
        session_data = self.get_service_account_data(session_id)
        if session_data:
            return session_data
        return dydb_cbr_user_sessions.document(session_id)

    def user_session_data(self, session_id):
        user_data = None
        if session_id:
            with capture_duration() as duration:
                raw_data     = self.raw_user_session_data(session_id)
                message = 'session not found'
        else:
            raw_data = None
            message = 'no session id provided'

        if raw_data:
            session_data         = raw_data.get('session_data', {})
            user_data            = raw_data.get('user_data'   , {})
            #session_auth_time    = session_data .get('auth_time'       )
            session_timestamp    = to_int(raw_data.get('timestamp')        )
            session_date         = timestamp_to_str_date(session_timestamp )
            session_time         = timestamp_to_str_time(session_timestamp )
            user_id              = session_data .get('sub'                 )
            user_name            = session_data .get('username'            )
            user_display_name    = user_data    .get('name'                ) or user_name
            user_created_date    = user_data    .get('user_create_date'    )
            user_email           = user_data    .get('email'               )
            user_enabled         = user_data    .get('enabled'             )
            user_security_groups = session_data .get('cognito:groups'      ) or []
            user_status          = user_data    .get('user_status'         )
            user_access          = self.calculate_user_access(user_security_groups)
            stats                = dict(duration__dydb = duration.seconds)
            user_data = dict(session_date         = session_date        ,
                             session_time         = session_time        ,
                             session_timestamp    = session_timestamp   ,
                             user_access          = user_access         ,
                             user_id              = user_id             ,
                             user_name            = user_name           ,
                             user_created_date    = user_created_date   ,
                             user_display_name    = user_display_name   ,
                             user_email           = user_email          ,
                             user_enabled         = user_enabled        ,
                             user_security_groups = user_security_groups,
                             user_status          = user_status         ,
                             stats                = stats               )

            message = 'session found'
        if user_data:
            return status_ok   (message=message, data=user_data)
        else:
            return status_error(message=message)

    def calculate_user_access(self, user_security_groups):
        is_admin     = 'CBR-Team' in user_security_groups
        is_customer  = False
        is_qa_user   = 'CBR-Bots' in user_security_groups or 'QA-Test-Users' in user_security_groups
        is_malicious = False
        is_user      = True

        return dict(is_admin     = is_admin     ,
                    is_customer  = is_customer  ,
                    is_qa_user   = is_qa_user   ,
                    is_malicious = is_malicious ,
                    is_user      = is_user      )

odin_cbr_user_session = Odin__CBR__User_Session()