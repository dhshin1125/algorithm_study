def solution(dartResult):
    dartResult = dartResult.replace('10', 'a')
    answer = []
    bonus = {'S':1,'D':2,'T':3}
    
    for i in dartResult:
        if i == 'a' or i.isdigit():
            answer.append(i if i.isdigit() else '10')
        elif i == 'S' or i == 'D' or i == 'T':
            number = answer.pop()
            answer.append(int(number) ** bonus[i])
        elif i == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == '#':
            answer[-1] = answer[-1] * (-1)
    return sum(answer)