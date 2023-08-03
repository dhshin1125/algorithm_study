import math
def solution(n):
    temp = []
    answer = 0
    while n >= 1:
        temp.append(math.floor(n%3))
        n /= 3
    temp = temp[::-1]

    for i in range(len(temp)):
        answer += (temp[i]*(3**(i)))
    return answer