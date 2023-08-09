def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        bin_arr = (bin(i | j))[2:].zfill(n)
        trans_arr = ["#" if i == '1' else " " for i in bin_arr]
        result = ''.join(trans_arr)
        answer.append(result)
    return answer