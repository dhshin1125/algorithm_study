def solution(lottos, win_nums):
    answer = []
    place = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    if sorted(lottos) == sorted(win_nums):
        return [1, 1]
    elif not any(l in win_nums for l in lottos) and sum(lottos) != 0:
        return [6, 6]

    zero_cnt = lottos.count(0)
    correct = len([l for l in lottos if l in win_nums])

    answer.append(place[correct + zero_cnt])  # 최고 순위
    answer.append(place[correct])  # 최저 순위

    return answer