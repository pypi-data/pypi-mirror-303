from ..RequestHandler import RequestHandler

class ChampionMasteryApi:
    ENDPOINTS = {
        'BY_PUUID': '/lol/champion-mastery/v4/champion-masteries/by-puuid/{}',
        'BY_PUUID_CHAMPION': '/lol/champion-mastery/v4/champion-masteries/by-puuid/{}/by-champion/{}',
        'BY_PUUID_TOP_CHAMPIONS': '/lol/champion-mastery/v4/champion-masteries/by-puuid/{}/top',
        'BY_PUUID_SUM_SCORE': '/lol/champion-mastery/v4/scores/by-puuid/{}',
    }

    def __init__(self, region, api_key):
        self.request_handler = RequestHandler(api_key, region, False)

    def by_puuid(self, puuid):
        return self.request_handler.make_request(self.ENDPOINTS['BY_PUUID'].format(puuid))

    def by_puuid_champion(self, puuid, champion_id):
        return self.request_handler.make_request(self.ENDPOINTS['BY_PUUID_CHAMPION'].format(puuid, champion_id))

    def by_puuid_top_champions(self, summoner_id, count=3):
        query_params = {k: v for k, v in locals().items() if v is not None and k != 'self'}
        return self.request_handler.make_request(self.ENDPOINTS['BY_PUUID_TOP_CHAMPIONS'].format(summoner_id))
    
    def by_puuid_sum_score(self, summoner_id, champion_id):
        return self.request_handler.make_request(self.ENDPOINTS['BY_PUUID_SUM_SCORE'].format(summoner_id, champion_id))
    