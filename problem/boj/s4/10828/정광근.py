import sys
N = int(sys.stdin.readline())
stack=[]
for _ in range(N):
    string = sys.stdin.readline().strip()
    if 'push' in string:
        pushs = string.split()
        stack.append(int(pushs[1]))
    elif 'pop' in string:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif string == 'size':
        print(len(stack))
    elif string == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif string == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)