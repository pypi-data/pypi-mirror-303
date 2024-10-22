from cbr_shared.config.CBR__Config                  import CBR__Config
from cbr_shared.config.CBR__Config__Active          import CBR__Config__Active
from osbot_utils.base_classes.Type_Safe             import Type_Safe
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from osbot_utils.utils.Env import load_dotenv, get_env


class Server_Config__CBR_Website(Type_Safe):
    override__aws_enabled : bool                        # todo: legacy : find a better way to handle this

    def __init__(self):
        super().__init__()
        load_dotenv()                   # make sure env vars are loaded

    # main objects
    @cache_on_self
    def cbr_config(self) -> CBR__Config:
        return self.cbr_config_active().cbr_config

    @cache_on_self
    def cbr_config_active(self) -> CBR__Config__Active:
        return self.cbr_config_data().create_cbr_config_active__from_current_config_file()

    @cache_on_self
    def cbr_config_data(self):
        from cbr_shared.config.CBR__Config__Data import CBR__Config__Data       # todo check if this is still needed here
        return CBR__Config__Data()

    @cache_on_self
    def cbr_site_info(self):
        from cbr_website_beta.config.CBR__Site_Info import CBR__Site_Info       # handle circular dependency on main cbr app import of this class
        return CBR__Site_Info()

    #@cache_on_self
    def cbr_site_info__data(self,reload_cache=False):
        return self.cbr_site_info(reload_cache=reload_cache).data()     # todo: fix bug related to the fact that reload_cache is currently not enforcing the value (i.e. as long as the param exists, the cache is reloaded which is not the behavior that we want)
                                                                        #       this is ok at the moment since there are not a lot of users of cbr_site_info

    # todo: refactor (legacy method)

    @staticmethod
    def current_execution_env():
        return get_env('EXECUTION_ENV', 'LOCAL')

    # helper methods

    def assets_dist(self):
        return self.cbr_config().assets_dist()

    def assets_root(self):
        return self.cbr_config().assets_root()

    def cbr_host__port(self):
        return self.cbr_site_info().cbr_host__port()

    def athena_path(self):
        return self.cbr_config().athena_path()

    def target_athena_url(self):
        return self.cbr_site_info().target_athena_url()

    def aws_disabled(self):
        if self.override__aws_enabled:
            return False
        return self.cbr_config().aws_disabled()

    def aws_enabled(self):
        if self.override__aws_enabled:
            return True
        return self.cbr_config().aws_enabled()

    def cbr_logo(self):
        return self.cbr_config().cbr_logo()

    def dev__capture_exceptions(self):
        return self.cbr_config().dev__capture_exceptions()

    def env(self):
        return self.cbr_config().env()

    def gta_enabled(self):
        return self.cbr_config().gta_enabled()

    def login_enabled(self):
        return self.cbr_config().login_enabled()

    def login_disabled(self):
        return self.cbr_config().login_disabled()

    def server_online(self):
        return self.cbr_site_info__data().get('server', {}).get('server_online', False)

    def session_cookie_httponly(self):
        return self.cbr_config().session_cookie_httponly()

    def remember_cookie_httponly(self):
        return self.cbr_config().remember_cookie_httponly()

    def remember_cookie_duration(self):
        return self.cbr_config().remember_cookie_duration()

    def s3_load_secrets(self):
        return self.cbr_config().s3_load_secrets()

    def s3_log_requests(self):
        return self.cbr_config().s3_log_requests()

    def s3_s3_use_minio(self):
        return self.cbr_config().s3_use_minio()

    def server_name(self):
        return self.cbr_config().server_name()

    def req_traces_enabled(self):
        return self.cbr_config().req_traces_enabled()

    def use_local_stack(self):
        return self.cbr_config().use_local_stack()

server_config__cbr_website = Server_Config__CBR_Website()