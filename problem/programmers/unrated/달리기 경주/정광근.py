def solution(players, callings):
    players_dict = dict()
    player = ''
    for count, id in enumerate(players):
        players_dict[id] = count

    for player in callings:
        idx = players_dict[player]
        #시간초과 심한 코드 
        #idx = players.index(player)
        players_dict[player] -= 1
        players_dict[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
    return players