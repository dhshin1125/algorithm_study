def solution(n, arr1, arr2):
    answer1 = []
    answer2 = []
    two1 = ''
    two2 = ''
    result = []
    for i,j in zip(arr1,arr2):
        if len(format(i,'b'))< n:
            two1 = '0'*(n-len(format(i,'b'))) + format(i,'b')
        else:
            two1 = format(i,'b')
        if len(format(j,'b'))< n:
            two2 = '0'*(n-len(format(j,'b'))) + format(j,'b')
        else:
            two2 = format(j,'b')
        answer1.append(two1)
        answer2.append(two2)
    for k,l in zip(answer1, answer2):
        temp = ''
        for i in range(n):
            if k[i] == l[i] == '0':
                temp += ' '
            else:
                temp += '#'
        result.append(temp)
                
    return result