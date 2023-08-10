T = int(input())

for i in range(T):
    string = input()
    stack = []
    for j in string:
        if j == '(':
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(j)
                break
                
    if not stack:
        print("YES")
    else:
        print("NO")