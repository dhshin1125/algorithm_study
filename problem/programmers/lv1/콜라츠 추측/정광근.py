def solution(num):
    answer = -1
    count = 0
        
    for i in range(500):
        if num == 1:
            break
        if num % 2 == 0:
            count += 1
            num = num / 2
        else:
            count += 1
            num = num * 3 + 1
    if count == 500:
        count = -1
        
    return count