import numpy as np
def solution(n, arr1, arr2):
    answer = []
    new_arr1 = []
    new_arr2 = []
    for a, b in zip(arr1, arr2):
        aa = format(a, 'b').zfill(n)
        bb = format(b, 'b').zfill(n)
        new_arr1.append(list(map(lambda x: int(x), aa)))
        new_arr2.append(list(map(lambda x: int(x), bb)))

    new_arr1, new_arr2 = np.array(new_arr1, dtype=object), np.array(new_arr2, dtype=object)
    output_arr = np.add(new_arr1, new_arr2)

    for i in range(n):
        for j in range(n):
            if output_arr[i][j] == 0:
                output_arr[i][j] = ' '
            else:
                output_arr[i][j] = '#'
        answer.append(''.join(output_arr[i]))
    return answer