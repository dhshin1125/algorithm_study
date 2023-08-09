def solution(nums):
    answer = 0
    comb = len(set(nums))

    return min(comb, len(nums) / 2)