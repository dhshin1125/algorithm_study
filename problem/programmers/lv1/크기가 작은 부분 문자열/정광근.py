def solution(t, p):
    answer = [] 
    count = 0
    for i in range(len(t) - len(p) + 1):
        answer.append(t[i:len(p)+i])
    for num in answer:
        if int(num) <= int(p):
            count += 1
    return count