from cbr_shared.aws.s3.S3_DB_Base       import S3_DB_Base
from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.utils.Files            import file_name


class S3__Files_Metadata(Type_Safe):
    s3_db         : S3_DB_Base
    parent_folder : str

    def load_from_l3(self):
        files_paths     = self.s3_db.s3_folder_files(folder=self.parent_folder, return_full_path=True)
        files_metadata  = []
        s3_bucket       = self.s3_db.s3_bucket()
        s3              = self.s3_db.s3()

        for file_path in files_paths:
            file_info = s3.file_details(bucket=s3_bucket, key=file_path)
            file_metadata = dict(file_name=file_name(file_path, check_if_exists=False),
                                 file_size=file_info.get('ContentLength'),
                                 metadata=file_info.get('Metadata'))
            files_metadata.append(file_metadata)
        return files_metadata