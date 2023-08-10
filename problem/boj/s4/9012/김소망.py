num = 0
n = int(input())
while True:
    paranth = list(map(str, input()))
    stack = [paranth[0]]
    for p in paranth[1:]:
        if stack and stack[-1] == '(' and p == ')':
            stack.pop()
        else: stack.append(p)
    if stack: print('NO')
    else: print('YES')
    num+= 1
    if num == n:
        break