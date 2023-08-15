import sys
n = int(input())

stack = []
command_dict = {'top': lambda: stack[-1] if stack else -1,
            'size': lambda: len(stack),
            'empty': lambda: 0 if stack else 1,
            'pop': lambda: stack.pop() if stack else -1}  # return이 있을 때만 되나

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    else: print(command_dict[command[0]]())