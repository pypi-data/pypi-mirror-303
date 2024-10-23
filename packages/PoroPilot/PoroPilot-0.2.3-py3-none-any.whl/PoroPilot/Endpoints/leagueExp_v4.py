from ..RequestHandler import RequestHandler

class LeagueExpApi:
    ENDPOINTS = {
        'BY_LEAGUE_ENTRIES': '/lol/league-exp/v4/entries/{}/{}/{}'
    }

    def __init__(self, region, api_key):
        self.request_handler = RequestHandler(api_key, region, False)

    def league_entries(self, queue,      # queue = RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
                            tier,        # tier = DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, IRON
                            division,    # division = I, II, III, IV
                            page=1): 
        
        query_params = {'page': page}
        return self.request_handler.make_request(self.ENDPOINTS['BY_LEAGUE_ENTRIES'].format(queue, tier, division), query_params=query_params)
    