from cbr_shared.aws.s3.S3__Files_Metadata import S3__Files_Metadata
from osbot_fast_api.api.Fast_API_Routes import Fast_API_Routes
from osbot_utils.context_managers.capture_duration import capture_duration

ROUTE_PATH__S3 = 's3'

class Routes__S3(Fast_API_Routes):
    tag       : str = ROUTE_PATH__S3

    def s3_db(self):
        raise NotImplementedError("The s3_db method is not implemented.")

    def setup_routes(self):
        self.add_route_get(self.list_folders       )
        self.add_route_get(self.list_files         )
        self.add_route_get(self.list_files_metadata)
        self.add_route_get(self.file_contents      )
        return self

    def list_folders(self, parent_folder='', return_full_path=False):
        return self.s3_db().s3_folder_list(folder=parent_folder, return_full_path=return_full_path)

    def list_files(self, parent_folder='', return_full_path=False):
        return self.s3_db().s3_folder_files(folder=parent_folder, return_full_path=return_full_path)

    def list_files_metadata(self, parent_folder=''):
        with capture_duration(action_name='list_files_metadata') as duration:
            s3_files_metadata = S3__Files_Metadata(s3_db=self.s3_db(), parent_folder=parent_folder)
            files_metadata    = s3_files_metadata.load_from_l3()
        result = dict(duration      = duration.json()    ,
                      file_count    = len(files_metadata),
                      files_metadata= files_metadata     )
        return result

    def file_contents(self, file_path):
        return self.s3_db().s3_file_data(s3_key=file_path)