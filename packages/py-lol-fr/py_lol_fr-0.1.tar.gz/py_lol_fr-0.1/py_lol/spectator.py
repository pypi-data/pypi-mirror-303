from py_lol.riot_api import RiotAPI




class Spectator:
    class _Participant:
        def __init__(self, data):
            self.puuid:str = data['puuid']
            self.teamId:int = data['teamId']
            self.spell1Id:int = data['spell1Id']
            self.spell2Id:int = data['spell2Id']
            self.championId:int = data['championId']
            self.profileIconId:int = data['profileIconId']
            self.riotId:str = data['riotId']
            self.bot:bool = data['bot']
            self.summonerId:str = data['summonerId']

    def __init__(self, api, data):
        self.api:RiotAPI = api
        self.queueId:int = data['gameQueueConfigId']
        self.gameMode:str = data['gameMode']
        self.matchId:str = f"{data['platformId']}_{data['gameId']}"
        self.gameStartTime:int = data['gameStartTime']
        self.gameLength:int = data['gameLength']
        self.participants:list[Spectator._Participant] = [Spectator._Participant(participant) for participant in data['participants']]
