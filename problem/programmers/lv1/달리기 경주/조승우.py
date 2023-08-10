def solution(players, callings):
    idx = {name: idx for idx, name in enumerate(players)}

    for c in callings:
        p1 = idx[c]
        if p1 - 1 < 0:
            continue

        swap(p1 - 1, p1, players, idx)

    return players


def swap(p1, p2, players, idx):
    players[p1], players[p2] = players[p2], players[p1]
    idx[players[p1]], idx[players[p2]] = idx[players[p2]], idx[players[p1]]