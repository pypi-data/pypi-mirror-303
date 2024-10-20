from cbr_athena.athena__fastapi.odin.server.routes.Routes__S3           import Routes__S3
from cbr_shared.cbr_sites.CBR_Site__Shared_Objects                      import cbr_site_shared_objects
from osbot_utils.decorators.methods.cache_on_self                       import cache_on_self


ROUTES_PATHS__S3__SERVERS = [ '/list-folders', '/list-files', '/list-files-metadata', '/file-contents']
ROUTE_PATH__S3__SERVERS   = 's3-servers'

class Routes__S3__Servers(Routes__S3):
    tag: str = ROUTE_PATH__S3__SERVERS

    @cache_on_self
    def s3_db(self):
        return cbr_site_shared_objects.s3_db_servers()                                  # this will create a bucket if it doesn't exist



