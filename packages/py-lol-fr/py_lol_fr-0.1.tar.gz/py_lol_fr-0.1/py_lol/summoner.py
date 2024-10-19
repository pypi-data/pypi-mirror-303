from py_lol.riot_api import RiotAPI

class Summoner:
    def __init__(self, api, data):
        self.api: RiotAPI = api
        self.id:str = data['id']
        self.accountId:str = data['accountId']
        self.puuid:str = data['puuid']
        self.profileIconId:int = data['profileIconId']
        self.revisionDate:int = data['revisionDate']
        self.summonerLevel:int = data['summonerLevel']


