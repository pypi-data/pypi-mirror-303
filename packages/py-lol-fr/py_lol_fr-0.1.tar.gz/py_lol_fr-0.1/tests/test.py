from py_lol.riot_services import RiotService

api = RiotService(api_key='RGAPI-262c2d47-ff25-4776-9fe5-78d6f1bdfc58')
acc = api.get_account_by_name_and_tag('Jhavixx', 'EUW')
summ = api.get_summoner_py_puuid(acc.puuid)

print(acc.puuid)

spec = api.get_spectator_by_puuid(summ.puuid)
print(spec.matchId)
# id = api.get_matchs_ids_by_puuid(summ1.puuid, count=1)[0]
# match = api.get_match_by_id(id)
# print(id)
# for participant in match.participants:
#     print(f"{participant.totalDamageDealtToChampions}")

