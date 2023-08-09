def solution(n, m):
    answer = []
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
            
    while(i > 0):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
        i += 1
    
    return answer 