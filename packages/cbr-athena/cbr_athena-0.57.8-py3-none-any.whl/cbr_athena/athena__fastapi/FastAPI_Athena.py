import uvicorn
from starlette.responses                                            import RedirectResponse

from cbr_athena.athena__fastapi.current_user.Current_User__Fast_API import Current_User__Fast_API
from cbr_athena.athena__fastapi.llms.LLMs__Fast_API                 import LLMs__Fast_API
from cbr_athena.athena__fastapi.middleware.add_logging              import Middleware_Logging
from cbr_athena.athena__fastapi.odin.api .Odin__FastAPI__API        import Odin__FastAPI__API
from cbr_athena.athena__fastapi.odin.chat.Odin__FastAPI__Chat       import Odin__FastAPI__Chat
from cbr_athena.athena__fastapi.odin.server.Odin__FastAPI__Server   import Odin__FastAPI__Server
from cbr_athena.athena__fastapi.odin.user.Odin__FastAPI__User       import Odin__FastAPI__User
from cbr_athena.athena__fastapi.routes.Routes__Auth                 import Routes__Auth
from cbr_athena.athena__fastapi.routes.Routes__Config               import Routes__Config
from cbr_athena.athena__fastapi.routes.Routes__Dev                  import Routes__Dev
from cbr_athena.athena__fastapi.routes.Routes__Logging              import Routes__Logging
from cbr_athena.athena__fastapi.routes.Routes__Ollama               import Routes__Ollama
from cbr_athena.athena__fastapi.routes.Routes__OpenAI               import Routes__OpenAI
from cbr_athena.athena__fastapi.routes.Routes__User                 import Routes__User
from osbot_fast_api.api.Fast_API                                    import Fast_API
from osbot_utils.decorators.methods.cache_on_self                   import cache_on_self


class FastAPI_Athena(Fast_API):

    def __enter__(self                           ): return self
    def __exit__ (self, exc_type, exc_val, exc_tb): return

    # @cache_on_self
    # def app(self):
    #     return FastAPI()

    def router(self):
        return self.app().router

    def setup(self):
        self.setup_routes()
        return self

    def add_middlewares(self, app):
        app.add_middleware(Middleware_Logging)
    #     if os.getenv('ENVIRONMENT') == 'Dev':
    #         app.add_middleware(
    #             CORSMiddleware,
    #             allow_origins    = ["*"],  # Allows all origins
    #             allow_credentials= True ,
    #             allow_methods    = ["*"],  # Allows all methods
    #             allow_headers    = ["*"],  # Allows all headers
    #         )
    #

    def setup_routes(self):
        self.router().get("/")(self.redirect_to_docs)
        app = self.app()

        self.add_middlewares(app)
        Routes__Auth    ().setup(app)
        self.add_routes (Routes__Config)
        Routes__Dev     ().setup(app)
        Routes__Logging ().setup(app)
        Routes__OpenAI  ().setup(app)
        Routes__Ollama  ().setup(app)
        Routes__User    ().setup(app)

        self.mount_other_fastapis()

    def mount_other_fastapis(self):                             # todo move out of this class
        self.odin__fastAPI__api    ().setup().mount(self.app())
        self.odin__fastAPI__chat   ().setup().mount(self.app())
        self.llms__fast_api        ().setup().mount(self.app())
        self.odin__fastapi__user   ().setup().mount(self.app())
        self.current_user__fast_api().setup().mount(self.app())

        # todo: remove the one below since once it has been replaced with the current-user apis
        self.odin_fastapi_server().setup().mount(self.app())   # todo: add a method called .setup_and_mount(self.app())

    @cache_on_self
    def current_user__fast_api(self):
        return Current_User__Fast_API()

    @cache_on_self
    def odin__fastAPI__api(self):
        return Odin__FastAPI__API()

    @cache_on_self
    def odin__fastAPI__chat(self):
        return Odin__FastAPI__Chat()

    @cache_on_self
    def odin__fastapi__user(self):
        return Odin__FastAPI__User()

    @cache_on_self
    def odin_fastapi_server(self):
        return Odin__FastAPI__Server()

    @cache_on_self
    def llms__fast_api(self):
        return LLMs__Fast_API()
    # def setup_middleware(self):
    #     if Utils.current_execution_env() == 'LOCAL':
    #         # Configure CORS for local server manually since this is done automatically by AWS Lambda
    #         self.app().add_middleware(CORSMiddleware,
    #                                   allow_origins     = ["*"]                         ,
    #                                   allow_credentials = True                          ,
    #                                   allow_methods     = ["GET", "POST", "HEAD"]       ,
    #                                   allow_headers     = ["Content-Type", "X-Requested-With", "Origin", "Accept", "Authorization"],
    #                                   expose_headers    = ["Content-Type", "X-Requested-With", "Origin", "Accept", "Authorization"])

    def run_in_lambda(self):
        lambda_host = '127.0.0.1'
        lambda_port = 8080
        self.setup()
        kwargs = dict(app  =  self.app(),
                      host = lambda_host,
                      port = lambda_port)
        uvicorn.run(**kwargs)

    # default routes
    async def redirect_to_docs(self):
        return RedirectResponse(url="/docs")
