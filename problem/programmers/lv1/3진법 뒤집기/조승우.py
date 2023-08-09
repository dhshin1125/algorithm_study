def solution(n):
    answer = ""
    while n != 0:
        div, mod = divmod(n, 3)
        answer += str(mod)
        n = div

    return int(answer,3)우