def solution(cards1, cards2, goal):
    answer = 'Yes'
    idx1=0
    idx2=0
    for i in goal:
        if len(cards1) > idx1 and i == cards1[idx1]:
            idx1 += 1
            print(idx1)
        elif len(cards2) > idx2 and i == cards2[idx2]:
            idx2 += 1
        else:
            return 'No'
    return answer