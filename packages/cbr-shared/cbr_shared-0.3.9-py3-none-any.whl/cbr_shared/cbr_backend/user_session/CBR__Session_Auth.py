from cbr_shared.cbr_backend.user_session.Odin__CBR__User_Session import Odin__CBR__User_Session
from osbot_utils.base_classes.Type_Safe                          import Type_Safe
from fastapi                                                     import Security, Request, HTTPException
from fastapi.security                                            import APIKeyHeader

api_key_header   = APIKeyHeader(name="Authorization", auto_error=False)


def cbr__fast_api__depends__admins_only(request: Request, session_id: str = Security(api_key_header)):
    if not request:
        raise HTTPException(status_code=501, detail="Request variable not available")
    cbr_session_auth.admins_only(request, session_id)


class CBR__Session_Auth(Type_Safe):
    odin_cbr_user_session : Odin__CBR__User_Session

    def session_data__from_cookie(self,request: Request):
        return self.session_data(request, session_id=None)

    def session_data(self, request: Request, session_id: str = Security(api_key_header)):

        if session_id is None:
            if 'CBR_TOKEN' in request.cookies:
                session_id = request.cookies.get('CBR_TOKEN')
                if '|' in session_id:                                   # for the cases where the admin is impersonating a session ID
                    session_id = session_id.split('|')[1]
        session_data = self.odin_cbr_user_session.user_session_data(session_id)

        if session_data.get('status') == 'ok':
            return session_data
        return {}

    def session_id_to_session_data(self,  request: Request):
        return self.session_data(request)

    def admins_only(self,request: Request, session_id: str = Security(api_key_header)):
        session_data = self.session_data(request, session_id)
        if session_data.get('data', {}).get('user_access', {}).get('is_admin'):
            return session_data
        else:
            raise HTTPException(status_code=401, detail="Unauthorized! Only admins can access this route")

cbr_session_auth = CBR__Session_Auth()