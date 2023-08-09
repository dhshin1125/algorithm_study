def solution(ingredient):
    answer = 0
    burger = []

    for i in ingredient:
        burger.append(i)
        if burger[-4:len(burger)] == [1,2,3,1]:
            burger.pop()
            burger.pop()
            burger.pop()
            burger.pop()
            answer += 1
    return answer
