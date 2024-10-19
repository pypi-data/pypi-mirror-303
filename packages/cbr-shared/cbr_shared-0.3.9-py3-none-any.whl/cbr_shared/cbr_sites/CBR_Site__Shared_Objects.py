from cbr_shared.aws.s3.S3_DB_Base__Disabled import S3_DB_Base__Disabled
from cbr_shared.cbr_backend.cbr.S3_DB__CBR import S3_DB__CBR
from cbr_shared.cbr_backend.chat_threads.S3_DB__Chat_Threads        import S3_DB__Chat_Threads
from cbr_shared.cbr_backend.chat_threads.S3_DB__Chat_Threads__Disabled import S3_DB__Chat_Threads__Disabled
from cbr_shared.cbr_backend.server_requests.S3_DB__Server_Requests  import S3_DB__Server_Requests
from cbr_shared.cbr_backend.server_requests.S3_DB__Server_Requests__Disabled import S3_DB__Server_Requests__Disabled
from cbr_shared.cbr_backend.servers.S3_DB__Servers                  import S3_DB__Servers
from cbr_shared.cbr_backend.servers.S3_DB__Servers__Disabled import S3_DB__Servers_Disabled
from cbr_shared.cbr_caches.CBR__Cache__LLM_Prompts                  import CBR__Cache__LLM_Prompts
from cbr_shared.config.CBR__Service_Accounts                        import CBR__Service_Accounts
from cbr_shared.config.Server_Config__CBR_Website                   import server_config__cbr_website
from osbot_utils.base_classes.Type_Safe                             import Type_Safe
from osbot_utils.decorators.methods.cache_on_self                   import cache_on_self


class CBR_Site__Shared_Objects(Type_Safe):

    @cache_on_self
    def cbr_cache_llm_prompts(self):
        return CBR__Cache__LLM_Prompts()

    @cache_on_self
    def cbr_service_accounts(self):
        return CBR__Service_Accounts()

    @cache_on_self
    def s3_cbr(self):
        if server_config__cbr_website.s3_log_requests() is False:
            return S3_DB_Base__Disabled()
        with  S3_DB__CBR() as _:
            _.setup()
            return _

    @cache_on_self
    def s3_db_server_requests(self):                                                # todo: refactor this code to remove duplicated code
        if server_config__cbr_website.s3_log_requests() is False:
            return S3_DB__Server_Requests__Disabled()
        server_name = server_config__cbr_website.server_name()
        kwargs      = dict(server_name =  server_name)
        with  S3_DB__Server_Requests(**kwargs)  as _:
            _.setup()                                                               # set up tasks, including creating target bucket if it doesn't exist
            _.s3_key_generator.use_request_path = True
            _.s3_key_generator.use_when         = True
            _.s3_key_generator.use_minutes      = False
            _.s3_key_generator.use_hours        = True
            return _

    @cache_on_self
    def s3_db_servers(self):                                                        # todo: refactor this code to remove duplicated code
        if server_config__cbr_website.s3_log_requests() is False:
            return S3_DB__Servers_Disabled()
        server_name = server_config__cbr_website.server_name()
        kwargs      = dict(server_name =  server_name)
        with  S3_DB__Servers(**kwargs)  as _:
            _.setup()                                                               # set up tasks, including creating target bucket if it doesn't exist
            _.s3_key_generator.use_request_path = False
            _.s3_key_generator.use_when         = True
            _.s3_key_generator.use_hours        = True
            _.s3_key_generator.use_minutes      = False

            return _

    @cache_on_self
    def s3_db_chat_threads(self):                                               # todo: refactor this code with the method s3_db_server_requests() since 95% is the same
        if server_config__cbr_website.s3_log_requests() is False:
            return S3_DB__Chat_Threads__Disabled()
        server_name = server_config__cbr_website.server_name()
        kwargs      = dict(server_name =  server_name)
        with  S3_DB__Chat_Threads(**kwargs)  as _:
            _.setup()                                                           # set up tasks, including creating target bucket if it doesn't exist
            _.s3_key_generator.use_request_path = False
            _.s3_key_generator.use_when         = True
            _.s3_key_generator.use_hours        = True
            _.s3_key_generator.use_minutes      = False
            return _

cbr_site_shared_objects = CBR_Site__Shared_Objects()
