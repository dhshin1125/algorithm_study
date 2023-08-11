import sys

N = int(sys.stdin.readline())
lst = [i for i in range(N,0,-1)]
stack = []
answer = []
flag = 0

for _ in range(N):
    num = int(sys.stdin.readline())
    while flag == 0:
        if stack and stack[-1] == num:
            stack.pop()
            answer.append('-')
            break
        else:
            if lst:
                stack.append(lst.pop())
                answer.append('+')
            else:
                flag = 1
                break
if flag == 0:
    for i in answer:
        print(i)
else:
    print("NO")
