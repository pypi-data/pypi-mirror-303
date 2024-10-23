from ..RequestHandler import RequestHandler

class LeagueApi:
    ENDPOINTS = {
        'BY_CHALL_QUEUE': '/lol/league/v4/challengerleagues/by-queue/{}',
        'BY_SUMMONER': '/lol/league/v4/entries/by-summoner/{}',
        'BY_QUEUE_TIER_DIVISION': '/lol/league/v4/entries/{}/{}/{}',
        'BY_GM_QUEUE': '/lol/league/v4/grandmasterleagues/by-queue/{}',
        'BY_LEAGUE': '/lol/league/v4/leagues/{}',
        'BY_MASTER_QUEUE': '/lol/league/v4/masterleagues/by-queue/{}'
    }

    def __init__(self, region, api_key):
        self.request_handler = RequestHandler(api_key, region, False)

    def chall_queue(self, queue): # queue = RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
        return self.request_handler.make_request(self.ENDPOINTS['BY_CHALL_QUEUE'].format(queue))
    
    def summoner(self, summoner_id):
        return self.request_handler.make_request(self.ENDPOINTS['BY_SUMMONER'].format(summoner_id))
    
    def league_entries(self, queue,      # queue = RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
                            tier,        # tier = DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, IRON
                            division,    # division = I, II, III, IV
                            page=1): 
        
        query_params = {'page': page}
        return self.request_handler.make_request(self.ENDPOINTS['BY_QUEUE_TIER_DIVISION'].format(queue, tier, division), query_params=query_params)
    
    def gm_queue(self, queue):
        return self.request_handler.make_request(self.ENDPOINTS['BY_GM_QUEUE'].format(queue))
    
    def league_id(self, league_uuid):
        return self.request_handler.make_request(self.ENDPOINTS['BY_LEAGUE'].format(league_uuid))
    
    def master_queue(self, queue):
        return self.request_handler.make_request(self.ENDPOINTS['BY_MASTER_QUEUE'].format(queue))