import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('([0-9]+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0: # i가 0보다 클때는 전에꺼 2배 해줌
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]] # 보너스로 제곱해주고 option에 맞게 곱해줌

    return sum(dart)