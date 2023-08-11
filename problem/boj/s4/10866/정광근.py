from collections import deque
import sys

N = int(sys.stdin.readline())

result = deque()
for _ in range(N):
    string = sys.stdin.readline().rstrip()
    if 'push_front' in string:
        pushs = string.split()
        result.appendleft(pushs[1])
    elif 'push_back' in string:
        pushs = string.split()
        result.append(pushs[1])
    elif 'pop_front' in string:
        if result:
            print(result.popleft())
        else:
            print(-1)
    elif 'pop_back' in string:
        if result:
            print(result.pop())
        else:
            print(-1)
    elif 'size' in string:
        print(len(result))
    elif 'empty' in string:
        if not result:
            print(1)
        else:
            print(0)
    elif 'front' in string:
        if result:
            print(result[0])
        else:
            print(-1)
    elif 'back' in string:
        if result:
            print(result[-1])
        else:
            print(-1)