from collections import defaultdict, Counter

def solution(N, stages):
    d = defaultdict(int)
    c = Counter(stages)

    live = len(stages)
    for i in range(1, N + 1):
        try:
            fail = c[i]
            d[i] = fail / live
            live -= fail
        except:
            d[i] = 0

    ret = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    ret = list(map(lambda x: x[0], ret))

    return ret
