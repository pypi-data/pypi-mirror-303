from typing import Any
import requests
from py_lol.enum.region import Region
from py_lol.enum.serveur import Server


class RiotAPI:
    def __init__(self, api_key:str, region:Region, server:Server):
        self.api_key = api_key
        self.region = region
        self.server = server
        self._headers = {
            "X-Riot-Token": self.api_key
        }

    ## Account
    def request_account_by_puuid(self, puuid:str) -> Any:
        url = f"https://{self.region.value}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
        return self.get_response_request(url)

    def request_account_by_name_and_tag(self, name:str, tag:str) -> Any:
        url = f"https://{self.region.value}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"
        return self.get_response_request(url)

    ## Summoner
    def request_summoner_py_puuid(self, puuid:str) -> Any:
        url = f"https://{self.server.value}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
        return self.get_response_request(url)

    def request_summoner_py_account_id(self, account_id:str) -> Any:
        url = f"https://{self.server.value}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{account_id}"
        return self.get_response_request(url)

    def request_summoner_py_id(self, id:str) -> Any:
        url = f"https://{self.server.value}.api.riotgames.com/lol/summoner/v4/summoners/{id}"
        return self.get_response_request(url)

    ## Champion Mastery
    def request_champion_masteries_by_puuid(self, puuid:str, champion_id:int = -1, top_count:int = -1) -> Any:
        if champion_id >= 0:
            url = f"https://{self.server.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
        elif top_count >= 0:
            url = f"https://{self.server.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count={top_count}"
        else:
            url = f"https://{self.server.value}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
        return self.get_response_request(url)

    ## League
    def request_league_summoner_by_summ_id(self, summoner_id:str) -> Any:
        url = f"https://{self.server.value}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
        return self.get_response_request(url)

    ## Match
    def request_matchs_ids_by_puuid(self, puuid:str, queueId:int = -1, queueType:str = "", start:int = 0, count:int = 20) -> Any:
        optional = ""
        if queueId >= 0:
            optional += f"&queue={queueId}"
        if queueType != "":
            optional += f"&type={queueType}"
        url = f"https://{self.region.value}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}{optional}"
        return self.get_response_request(url)

    def request_match_by_id(self, match_id:str) -> Any:
        url = f"https://{self.region.value}.api.riotgames.com/lol/match/v5/matches/{match_id}"
        return self.get_response_request(url)

    def request_spectator_by_puuid(self, puuid:str) -> Any:
        url = f"https://{self.server.value}.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/{puuid}"
        return self.get_response_request(url)
    
    def get_response_request(self, url:str) -> Any:
        response = requests.get(url, headers=self._headers)
        if response.status_code == 200:
            return response.json()
        return None
