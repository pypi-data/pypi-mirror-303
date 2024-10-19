from py_lol.riot_api import RiotAPI

class Account:
    def __init__(self, api, data):
        self.api:RiotAPI = api
        self.puuid: str = data['puuid']
        self.gameName: str = data['gameName']
        self.tagLine: str = data['tagLine']