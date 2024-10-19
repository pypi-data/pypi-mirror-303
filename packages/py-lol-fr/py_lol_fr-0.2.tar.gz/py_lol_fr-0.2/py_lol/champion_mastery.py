from py_lol.riot_api import RiotAPI

class ChampionMastery:
    def __init__(self, api, data):
        self.api:RiotAPI = api
        self.puuid: str = data['puuid']
        self.championId: int = data['championId']
        self.championLevel: int = data['championLevel']
        self.championPoints: int = data['championPoints']
        self.lastPlayTime: int = data['lastPlayTime']
        self.championPointsSinceLastLevel: int = data['championPointsSinceLastLevel']
        self.championPointsUntilNextLevel: int = data['championPointsUntilNextLevel']
        self.markRequiredForNextLevel: int = data['markRequiredForNextLevel']
        self.tokensEarned: int = data['tokensEarned']
        self.championSeasonMilestone: int = data['championSeasonMilestone']
        self.milestoneGrades: list = data['milestoneGrades']
        self.nextSeasonMilestone: dict = data['nextSeasonMilestone']
