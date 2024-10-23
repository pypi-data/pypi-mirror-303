from cbr_shared.aws.s3.S3_DB_Base                   import S3_DB_Base

S3_FOLDER__USERS_SESSIONS        = 'users_sessions'
S3_FOLDER__GUESTS                = 'guests'

class S3_DB__CBR(S3_DB_Base):                           # todo: refactor the need of this generic class/bucket into specific buckets
    bucket_name__suffix : str = 'server-data'
    bucket_name__prefix : str = 'cyber-boardroom'

    def s3_folder_guests(self):
        return S3_FOLDER__GUESTS

    def s3_folder_users_sessions(self):
        return S3_FOLDER__USERS_SESSIONS