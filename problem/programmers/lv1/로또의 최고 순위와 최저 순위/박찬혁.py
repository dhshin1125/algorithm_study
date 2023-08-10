def solution(lottos, win_nums):
    # 첫번째 맞춘개수 : 등수
    # grade = {6:1, 5:2, 4:3, 3:4 , 2:5 , 1:6, 0:6}
    # ret =  len(set(lottos) & set(win_nums))
    # bonus = lottos.count(0)
    # return [grade[ret + bonus], grade[ret]]
    answer = [0] * 2
    correct = [x for x in lottos if x in win_nums]
    answer[1] = 7 - len(correct) if len(correct) > 1 else 6
    answer[0] = 7 - (len(correct) + lottos.count(0)) if len(correct) + lottos.count(0) > 1 else 6

    # 최대 등수 = 0의 개수를 더한 거
    # 최소 등수  = correct 로 일치하는 개수 --> 맞는 개수가 1 이하일 경우는 그냥 자동 6등

    return answer