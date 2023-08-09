# 스택 관련
# 1 2 3 --> 3 2 1
# 파이썬에서 스택 자료구조는 list()로 사용한다
# apppend() 끝에서 부터 채워넣는다
# pop() 끝에 있는 놈을 꺼낸다..

# 햄버거의 조건 [빵, 야채, 고기, 빵]

# 제거 전 : [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]
# 제거 후 : [야채, 빵, 야채, 고기, 빵]
# 제거 후 : [야채]
# 2

# [빵 고기 야채 빵 고 빵 야채 빵 고기]
# 0

def solution(ingredient):
    answer = 0
    stack = [] # list()
    burger = [1, 2, 3, 1] # [빵 고기 야채 빵] 패턴
    idx = 0
    for value in ingredient:
        stack.append(value)
        if len(stack) >= 4:
            isburger = stack[-4:]
            print(stack[-4:-1])
            if isburger == burger:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1
    return answer