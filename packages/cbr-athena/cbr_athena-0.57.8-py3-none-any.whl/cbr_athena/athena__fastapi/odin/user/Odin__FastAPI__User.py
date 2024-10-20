from osbot_fast_api.api.Fast_API import Fast_API

from cbr_athena.athena__fastapi.odin.user.routes.Routes__User_Session import Routes__User_Session


class Odin__FastAPI__User(Fast_API):
    base_path      : str = '/user'
    default_routes : bool = False

    def setup_routes(self):
        self.add_routes(Routes__User_Session)
