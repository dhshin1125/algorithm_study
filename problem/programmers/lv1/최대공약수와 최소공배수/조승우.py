from math import *
def solution(n, m):
    return [gcd(n,m), n * m // gcd(n,m) ]