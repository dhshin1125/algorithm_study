def solution(number, limit, power):
    cnt_list = [0] * number
    for num in range(1, number+1): # 각 기사단원의
        for i in range(1, int(num**0.5) +1): # 약수 찾기
            if num%i == 0:   # 약수가
                if i == (num**0.5): #sqrt(num) == i면 i*i == num이니깐
                    cnt_list[num-1] += 1 # 한번만 나옴
                else: # 다른 경우에는 자기 자신도 포함
                    print(num, i)
                    cnt_list[num-1] += 2 # 두번
        if cnt_list[num-1] > limit:
            cnt_list[num-1] = power
    return sum(cnt_list)