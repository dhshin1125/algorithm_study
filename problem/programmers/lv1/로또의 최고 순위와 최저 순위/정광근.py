def solution(lottos, win_nums):
    answer = [0,0]
    count = 0
    rank = [6,6,5,4,3,2,1]
    for i in win_nums:
        if i in lottos:
            count += 1
    
    return [rank[count + lottos.count(0)],rank[count]]