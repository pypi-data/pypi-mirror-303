from ..RequestHandler import RequestHandler

class AccountApi:
    ENDPOINTS = {
        'BY_PUUID': '/riot/account/v1/accounts/by-puuid/{PUUID}',
        'BY_GAMENAME': '/riot/account/v1/accounts/by-riot-id/{gamename}/{tagline}',
        'ACTIVE_SHARD': '/riot/account/v1/active-shards//by-game/{game}/by-puuid/{PUUID}'
    }   

    def __init__(self, region, api_key):
        self.request_handler = RequestHandler(api_key, region, True)

    def by_puuid(self, puuid):
        return self.request_handler.make_request(self.ENDPOINTS['BY_PUUID'].format(puuid))
    
    def by_gamename(self, gamename, tagline):
        return self.request_handler.make_request(self.ENDPOINTS['BY_GAMENAME'].format(gamename=gamename, tagline=tagline))