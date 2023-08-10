def solution(N, stages):
    answer = {id:0 for id in range(1,N+1)}
    den = len(stages)
    for i in range(N):
        den -= stages.count(i)
        if den != 0:
            answer[i + 1] = stages.count(i + 1) / den
    return sorted(answer, key=lambda x: answer[x], reverse=True)