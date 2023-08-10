from math import *

# 에라토스테네스의 체 알고리즘
# 1 2 4
# (1,4), (2,2), (4,1)
# 제곱근 기점으로 대칭이다.. 따라서 root 만큼만 하자...
# n -> log n

def get_divior_count(target):
    count = set()
    for i in range(1, int(sqrt(target)) + 1):
        if target % i == 0:
            count.add(i)
            count.add(target//i)
    return len(count)


def solution(number, limit, power):
    hero_list = [get_divior_count(i) if get_divior_count(i) <= limit else power for i in range(1, number + 1)]
    return sum(hero_list)