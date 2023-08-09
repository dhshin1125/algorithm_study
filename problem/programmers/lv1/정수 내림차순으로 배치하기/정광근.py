def solution(n):
    answer = list(map(int, str(n)))
    answer.sort(reverse=True)
    answer = ''.join(map(str, answer)) 
      
    return int(answer)