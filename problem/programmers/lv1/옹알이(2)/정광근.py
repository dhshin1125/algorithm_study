def solution(babbling):
    answer = []
    result = 0
    pro_lst =  ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for pro in pro_lst:
            if pro * 2 not in i:
                i = i.replace(pro,' ')
        i = i.replace(' ','')
        answer.append(i)
    for blank in answer:
        if blank == '':
            result += 1
            
    return result