def solution(t, p):
    answer = 0
    end = len(p)
    p = int(p)
    start = 0
    while True:
        if int(t[start:end]) <= p:
            answer += 1
        start += 1
        end += 1
        if end == len(t)+1:
            break
    return answer