from py_lol.riot_api import RiotAPI

class League:
    def __init__(self, api, data):
        self.api:RiotAPI = api
        self.leagueId: str = data['leagueId']
        self.queueType: str = data['queueType']
        self.tier: str = data['tier']
        self.rank: str = data['rank']
        self.summonerId: str = data['summonerId']
        self.leaguePoints: int = data['leaguePoints']
        self.wins: int = data['wins']
        self.losses: int = data['losses']
        self.veteran: bool = data['veteran']
        self.inactive: bool = data['inactive']
        self.freshBlood: bool = data['freshBlood']
        self.hotStreak: bool = data['hotStreak']