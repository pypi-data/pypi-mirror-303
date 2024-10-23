from ..RequestHandler import RequestHandler

# TODO

# Faire une classe API ? 
# Pour la passer en child sur les endpoints de l'api
# ex SummonerApi devient SummonerApi(Api?)
# avec seulement(debug)?
# puisque la région serait choisie par la classe Api? directement
# et du coup il resterait rien ? en __init__? 
# Puisque region, key, url et requestHandler
# serait gérés par la classe Api directement 

class SummonerApi:
    ENDPOINTS = {
        'BY_ACCOUNT': '/lol/summoner/v4/summoners/by-account/{}',
        'BY_NAME': '/lol/summoner/v4/summoners/by-name/{}',
        'BY_PUUID': '/lol/summoner/v4/summoners/by-puuid/{}',
        'BY_ID': '/lol/summoner/v4/summoners/{}'
    }
    
    def __init__(self, region, api_key):
        self.request_handler = RequestHandler(api_key, region, False)

    def by_account(self, encrypted_account_id):
        return self.request_handler.make_request(self.ENDPOINTS['BY_ACCOUNT'].format(encrypted_account_id))

    def by_name(self, summoner_name):
        return self.request_handler.make_request(self.ENDPOINTS['BY_NAME'].format(summoner_name))
    
    def by_puuid(self, encrypted_puuid):
        return self.request_handler.make_request(self.ENDPOINTS['BY_PUUID'].format(encrypted_puuid))

    def by_id(self, encrypted_summoner_id):
        return self.request_handler.make_request(self.ENDPOINTS['BY_ID'].format(encrypted_summoner_id))