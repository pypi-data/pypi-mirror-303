from py_lol.enum.region import Region
from py_lol.enum.serveur import Server
from py_lol.league import League
from py_lol.match import Match
from py_lol.riot_api import RiotAPI
from py_lol.account import Account
from py_lol.spectator import Spectator
from py_lol.summoner import Summoner
from py_lol.champion_mastery import ChampionMastery


class RiotService:
    def __init__(self, api_key:str, region:Region = Region.EUROPE, server:Server = Server.EUW1):
        self.api = RiotAPI(api_key, region, server)

    ## Account
    def get_account_by_name_and_tag(self, name:str, tag:str) -> Account | None:
        """
        :param name: nom d'un compte riot game
        :param tag: tag d'un compte riot game
        :return: Un objet Account ou None si il n'a pas été trouvé

        Permet d'obtenir les informations d'un compte riot game
        grâce à son nom et son tag (Exemple#EUW).
        """
        account_data = self.api.request_account_by_name_and_tag(name, tag)
        if account_data:
            return Account(self.api, account_data)
        return None

    def get_account_by_puuid(self, puuid:str) -> Account | None:
        """
        :param puuid: puuid d'un compte riot game
        :return: Un objet Account ou None si il n'a pas été trouvé

        Permet d'obtenir les informations d'un compte riot game
        grâce à son puuid.
        """
        account_data = self.api.request_account_by_puuid(puuid)
        if account_data:
            return Account(self.api, account_data)
        return None

    ## Summoner
    def get_summoner_py_puuid(self, puuid:str) -> Summoner | None:
        """
        :param puuid: puuid d'un summoner
        :return: Un objet Summoner ou None si il n'a pas été trouvé

        Permet d'obtenir les informations d'un summoner
        grâce à son puuid.
        """
        summoner_data = self.api.request_summoner_py_puuid(puuid)
        if summoner_data:
            return Summoner(self.api, summoner_data)
        return None

    def get_summoner_py_account_id(self, account_id:str) -> Summoner | None:
        """
        :param account_id: id d'un compte riot game
        :return: Un objet Summoner ou None si il n'a pas été trouvé

        Permet d'obtenir les informations d'un summoner
        grâce à son account id.
        """
        summoner_data = self.api.request_summoner_py_account_id(account_id)
        if summoner_data:
            return Summoner(self.api, summoner_data)
        return None

    def get_summoner_py_id(self, id:str) -> Summoner | None:
        """
        :param id: id d'un summoner
        :return: Un objet Summoner ou None si il n'a pas été trouvé

        Permet d'obtenir les informations d'un summoner
        grâce à son id.
        """
        summoner_data = self.api.request_summoner_py_id(id)
        if summoner_data:
            return Summoner(self.api, summoner_data)
        return None

    ## Champion Mastery
    def get_champion_masteries_by_puuid(self, puuid: str, champion_id: int = -1, top_count: int = -1) -> list[ChampionMastery]:
        """
        :param puuid: puuid d'un summoner.
        :param champion_id: id d'un champion (optionel).
        :param top_count: nombre de meilleurs champions (optionel).
        :return: liste des champions avec les infos de maîtrise (si vide = pas trouvé).

        Permet d'obtenir les maîtrise de champion d'un summoner
        grâce à son puuid.

        Si vous mettez le champion_id et le top_count, le champion_id va être choisis en priorité.
        """
        champion_masteries_data = self.api.request_champion_masteries_by_puuid(puuid, champion_id, top_count)
        liste_champions = []
        if champion_masteries_data:
            if isinstance(champion_masteries_data, list):
                for champion_data in champion_masteries_data:
                    liste_champions.append(ChampionMastery(self.api, champion_data))
            else:
                liste_champions = [ChampionMastery(self.api, champion_masteries_data)]
        return liste_champions

    ## League
    def get_league_summoner_by_summ_id(self, summoner_id:str) -> list[League]:
        """
        :param summoner_id: l'id d'un summoner.
        :return: La liste des classements du summoner

        Permet d'obtenir les classements du summoner
        """
        league_summoner_data = self.api.request_league_summoner_by_summ_id(summoner_id)
        liste_leagues = []
        if league_summoner_data:
            if isinstance(league_summoner_data, list):
                for league_data in league_summoner_data:
                    liste_leagues.append(League(self.api, league_data))
            else:
                liste_leagues = [League(self.api, league_summoner_data)]
        return liste_leagues

    def get_matchs_ids_by_puuid(self, puuid:str, queueId:int = -1, queueType:str = "", start:int = 0, count:int = 20) -> list[str]:
        """
        :param puuid: puuid d'un summoner.
        :param queueId: id d'un queue (optionel).
        :param queueType: type d'un queue (optionel).
        :param start: nombre de matchs récents pas pris en compte (optionel).
        :param count: nombre de matchs (optionel).
        :return: liste des ids de matchs du summoner.
        """
        return self.api.request_matchs_ids_by_puuid(puuid, queueId, queueType, start, count)

    def get_match_by_id(self, match_id:str) -> Match | None:
        """
        :param match_id:
        :return:
        """
        data_match = self.api.request_match_by_id(match_id)
        if data_match:
            return Match(self.api, data_match)
        return None

    def get_spectator_by_puuid(self, puuid:str) -> Spectator | None:
        """
        :param puuid:
        :return:
        """
        data_spectator = self.api.request_spectator_by_puuid(puuid)
        if data_spectator:
            return Spectator(self.api, data_spectator)
        return None
