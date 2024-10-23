from ..RequestHandler import RequestHandler

class LolStatusApi:
    ENDPOINTS = {
        'BY_REGION': '/lol/status/v4/platform-data'
    }

    def __init__(self, region, api_key):
        self.request_handler = RequestHandler(api_key, region, False)

    def region(self):
        return self.request_handler.make_request(self.ENDPOINTS['BY_REGION'])
    