def solution(n):
    num = sorted(list(str(n)), reverse = True)
    return int(''.join(num))