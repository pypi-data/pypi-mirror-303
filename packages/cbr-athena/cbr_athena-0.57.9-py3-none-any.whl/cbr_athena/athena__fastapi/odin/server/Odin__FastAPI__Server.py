import traceback
from fastapi                                                                    import Depends
from cbr_athena.athena__fastapi.odin.server.routes.Routes__S3__Chat_Threads     import Routes__S3__Chat_Threads
from cbr_athena.athena__fastapi.odin.server.routes.Routes__S3__Server_Requests  import Routes__S3__Server_Requests
from cbr_athena.athena__fastapi.odin.server.routes.Routes__S3__Servers          import Routes__S3__Servers
from cbr_athena.athena__fastapi.odin.server.routes.Routes__Server__Requests     import Routes__Server__Requests
from cbr_shared.cbr_backend.user_session.CBR__Session_Auth                      import cbr__fast_api__depends__admins_only
from osbot_fast_api.api.Fast_API                                                import Fast_API
from osbot_utils.decorators.methods.cache_on_self                               import cache_on_self


class Odin__FastAPI__Server(Fast_API):
    base_path      : str  = '/server'
    default_routes : bool = False

    @cache_on_self
    def app(self, **kwargs):                                                        # todo: add native super to Fast_API for adding dependencies
        kwargs['dependencies'] = [Depends(cbr__fast_api__depends__admins_only)]
        app = super().app(**kwargs)
        return app

    def setup_routes(self):
        self.add_routes(Routes__Server__Requests   )
        self.add_routes(Routes__S3__Server_Requests)
        self.add_routes(Routes__S3__Chat_Threads   )
        self.add_routes(Routes__S3__Servers        )
