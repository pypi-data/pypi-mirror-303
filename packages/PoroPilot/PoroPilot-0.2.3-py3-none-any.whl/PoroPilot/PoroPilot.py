from .Endpoints import *

class PoroPilot:
    def __init__(self, api_key, region):
        # TODO: add api class
        # self.api = Api(region, api_key)
        # self.summoner = SummonerApi()

        self.summoner = summoner_v4.SummonerApi(region, api_key)
        self.match = match_v5.MatchApi(region, api_key)
        self.champion = champion_v3.ChampionApi(region, api_key)
        self.mastery = championMastery_v4.ChampionMasteryApi(region, api_key)
        self.league = league_v4.LeagueApi(region, api_key)
        self.spectator = spectator_v4.SpectatorApi(region, api_key)
        self.league_exp = leagueExp_v4.LeagueExpApi(region, api_key)
        self.lol_status = lolStatus_v4.LolStatusApi(region, api_key)
        self.account = account_v1.AccountApi(region, api_key)
        
        


    
    
    

    
    # get winrate ?
    # general functions to get stats ?
    # get games played with count ?
    # stats by champion ?
    # stats by role ?
    # average stats ?
    # random games picked ?
    # change champion id to champion name ?