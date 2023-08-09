def solution(babbling):
    answer = 0
    bb = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        for b in bb:
            if i == b:
                answer += 1
            elif b in i and b*2 not in i:
                i = i.replace(b, ' ')
                if len(i.strip()) == 0 : answer += 1
    return answer