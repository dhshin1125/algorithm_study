def solution(survey, choices):
    category_dict = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    category_list = [['R','T'],['C','F'],['J','M'],['A','N']]
    answer = ""
    
    for sur,choice in zip(survey,choices):
        if choice < 4:
            category_dict[sur[:1]] += abs(choice - 4)
        else:
            category_dict[sur[1:]] += abs(choice - 4)          
            
    for i in category_list:
        if category_dict[i[0]] < category_dict[i[1]]:
            answer += i[1]
        else:
            answer += i[0]
    
    
    return answer