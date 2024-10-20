from typing                                 import Literal
from fastapi                                import Request
from fastapi.security                       import APIKeyHeader
from cbr_athena.odin.data.Data__Http_Events import Data__Http_Events
from osbot_fast_api.api.Fast_API_Routes     import Fast_API_Routes

ROUTES_PATHS__SERVER_REQUESTS = ['/request-data',  '/requests-data']
ROUTE_PATH__SERVER_REQUESTS   = 'requests'

api_key_header      = APIKeyHeader(name="Authorization", auto_error=False)
LITERAL_RETURN_TYPE = Literal['dict', 'table', 'list']

class Routes__Server__Requests(Fast_API_Routes):
    tag             : str = ROUTE_PATH__SERVER_REQUESTS

    def convert_to_return_type(self, data, return_type:LITERAL_RETURN_TYPE):
        if return_type == 'table':
            return self.convert_to_table(data)
        return data

    def convert_to_table(self, data):
        if data and type(data) is list:
            headers = list(data[0].keys())                                  # Extract headers from the first dictionary
            rows    = [list(item.values()) for item in data]                      # Extract rows by getting the values of each dictionary
        else:
            headers = []
            rows    = []
        return dict(headers = headers,
                    rows    = rows   )

    def data_http_events(self, request: Request) -> Data__Http_Events:
        if request:
            if hasattr(request.state, 'http_events'):
                http_events = request.state.http_events
                return Data__Http_Events(http_events=http_events)

    # routes
    def request_data(self,  request: Request = None, request_id: str='', request_index: int=-1,return_type: LITERAL_RETURN_TYPE  = 'json'):
        data = self.data_http_events(request).request_data(request_id=request_id, request_index=request_index)
        return self.convert_to_return_type(data, return_type)

    def requests_data(self, request: Request = None, return_type:LITERAL_RETURN_TYPE='json'):
        data = self.data_http_events(request).requests_data()
        return self.convert_to_return_type(data, return_type)

    def setup_routes(self):
        self.add_route_get(self.request_data )
        self.add_route_get(self.requests_data)
        return self