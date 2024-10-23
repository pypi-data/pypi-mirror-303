from ..RequestHandler import RequestHandler

class SpectatorApi:
    ENDPOINTS = {
        'BY_SUMMONER': '/lol/spectator/v4/active-games/by-summoner/{}',
        'BY_FEATURED_GAMES': '/lol/spectator/v4/featured-games'
    }

    def __init__(self, region, api_key):
        self.request_handler = RequestHandler(api_key, region, False)

    def by_summoner(self, summoner_id):
        return self.request_handler.make_request(self.ENDPOINTS['BY_SUMMONER'].format(summoner_id))
    
    def feature_games(self):
        return self.request_handler.make_request(self.ENDPOINTS['BY_FEATURED_GAMES'])