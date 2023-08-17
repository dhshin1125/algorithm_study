import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    string = sys.stdin.readline().rstrip()

    if 'push' in string:
        pushs = string.split()
        queue.append(int(pushs[1]))
    elif 'pop' in string:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif 'size' in string:
        print(len(queue))
    elif 'empty' in string:
        if queue:
            print(0)
        else:
            print(1)
    elif 'front' in string:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in string:
        if queue:
            print(queue[-1])
        else:
            print(-1)