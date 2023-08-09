def solution(players, callings):
    player_idx = {players: idx for idx, players in enumerate(players)}
    for c in callings:
        cur_idx = player_idx[c]
        player_idx[players[cur_idx]] -= 1
        player_idx[players[cur_idx - 1]] += 1

        players[cur_idx] = players[cur_idx - 1]
        players[cur_idx - 1] = c

    return players