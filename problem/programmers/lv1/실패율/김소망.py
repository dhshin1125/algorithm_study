def solution(N, stages):
    answer = []
    failure = {}
    stages = sorted(stages)

    for i in range(1, N + 1):
        if i in stages: stages = stages[stages.index(i):]
        numera = stages.count(i)
        denom = len(stages)
        if numera == 0 and denom == 0:
            failure[i] = 0
        else:
            failure[i] = (numera / denom)

    answer = sorted(failure, key=failure.get, reverse=True)
    return answer