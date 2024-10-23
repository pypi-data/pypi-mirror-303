from ..RequestHandler import RequestHandler

class ChampionApi:
    ENDPOINTS = {
        'CHAMP_ROTATION': '/lol/platform/v3/champion-rotations'
    }

    def __init__(self, region, api_key):
        self.request_handler = RequestHandler(api_key, region, False)

    def champion_rotation(self):
        return self.request_handler.make_request(self.ENDPOINTS['CHAMP_ROTATION'])