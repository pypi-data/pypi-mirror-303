from cbr_athena.athena__fastapi.odin.server.routes.Routes__S3    import Routes__S3
from cbr_shared.cbr_backend.chat_threads.S3__Chat_Threads import S3__Chat_Threads
from cbr_shared.cbr_sites.CBR_Site__Shared_Objects               import cbr_site_shared_objects
from osbot_utils.decorators.methods.cache_on_self                import cache_on_self


ROUTES_PATHS__S3__CHAT_THREADS = [ '/list-folders', '/list-files', '/list-files-metadata', '/file-contents']
ROUTE_PATH__S3__CHAT_THREADS   = 's3-chat-threads'

class Routes__S3__Chat_Threads(Routes__S3):
    tag: str = ROUTE_PATH__S3__CHAT_THREADS

    @cache_on_self
    def s3_db(self):
        return cbr_site_shared_objects.s3_db_chat_threads()                                  # this will create a bucket if it doesn't exist

    @cache_on_self
    def s3_chat_threads(self):
        return S3__Chat_Threads()

    def all_chat_threads_for_today(self, day=None):
        from osbot_utils.utils.Dev import pprint
        pprint(day)
        return self.s3_chat_threads().all_chat_threads_for_day(day)

    def setup_routes(self):
        super().setup_routes()
        self.add_route_get(self.all_chat_threads_for_today)


