def solution(s):
    answer = True
    stack = []
    for j in s:
        if j == '(':
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(j)
                break
                
    if not stack:
        answer = True
    else:
        answer = False

    return answer