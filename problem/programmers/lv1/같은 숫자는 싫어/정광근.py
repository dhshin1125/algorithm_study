def solution(arr):
    answer = []
    a = -1
    for i in arr:
        if a != i:
            a = i
            answer.append(i)
    return answer