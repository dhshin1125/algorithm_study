import re
def solution(n, arr1, arr2):
    map_num = [0]*n
    for i in range(n):
        map_num[i] = "0" * (n - len(re.sub("0b", "", bin(arr1[i] | arr2[i])))) + re.sub("0b", "", bin(arr1[i] | arr2[i]))
        map_num[i] = re.sub("1","#", map_num[i])
        map_num[i] = re.sub("0"," ", map_num[i])
    return map_num