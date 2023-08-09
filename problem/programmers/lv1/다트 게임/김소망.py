import re
def solution(dartResult):
    answer = 0
    dartResult = re.findall(r'\d+[A-Za-z]|[*#]', dartResult)
    scores = []

    for i in range(len(dartResult)):
        if 'S' in dartResult[i]:
            scores.append(int(dartResult[i][:-1])**1)
        elif 'D' in dartResult[i]:
            scores.append(int(dartResult[i][:-1])**2)
        elif 'T' in dartResult[i]:
            scores.append(int(dartResult[i][:-1])**3)
        elif dartResult[i] == '*':
            scores[-1]*=2
            if len(scores) > 1:
                scores[-2]*=2
        elif dartResult[i] == '#':
            scores[-1]*=(-1)
    return sum(scores)