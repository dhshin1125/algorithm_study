from collections import Counter

def solution(nums):
    c = Counter(nums)
    if len(c.keys()) >= len(nums) // 2:
        return len(nums) // 2
    return len(c.keys())