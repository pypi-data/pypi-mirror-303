
from cbr_shared.cbr_sites.CBR_Site__Shared_Objects  import cbr_site_shared_objects
from osbot_utils.base_classes.Type_Safe             import Type_Safe


class S3__Chat_Threads(Type_Safe):

    def s3_db_chat_threads(self):
        return cbr_site_shared_objects.s3_db_chat_threads()

    def all_chat_threads_for_today(self):
        return self.all_chat_threads_for_day()

    def all_chat_threads_for_day(self, day=None):
        with self.s3_db_chat_threads()  as _:
            s3_folder = _.s3_key_generator.s3_folder__for_day(day)
            return self.s3_db_chat_threads().s3_folder_files(s3_folder, include_sub_folders=True)
