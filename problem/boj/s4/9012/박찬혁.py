T = int(input())
for i in range(T):
    PS = input()
    PS_list = []
    VPS = True

    for word in PS:
        if word == '(':
            PS_list.append('(')
        if word == ')':
            if PS_list:
                PS_list.pop()
            elif not PS_list:
                VPS = False
                break
    if not PS_list and VPS:
        print('YES')
    elif PS_list or not VPS:
        print('NO')

