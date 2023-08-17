from collections import deque

import sys

N, M = map(int,sys.stdin.readline().split())

queue = deque()

num = list(map(int,sys.stdin.readline().split()))

for i in range(1,N+1):
    queue.append(i)

count = 0

for j in num:
    while True:
        if j == queue[0]:
            queue.popleft()
            break
        else:
            if queue.index(j) <= len(queue)/2:
                queue.rotate(-1)
                count += 1
            else:
                queue.rotate(1)
                count += 1
print(count)


