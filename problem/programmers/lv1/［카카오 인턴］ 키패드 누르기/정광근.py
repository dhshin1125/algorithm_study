def solution(numbers, hand):
    answer = ''
    location = {'L': 10, 'R': 12}
    for i in numbers:
        if i in (1,4,7):
            location['L'] = i
            answer += 'L'
        elif i in (3,6,9):
            location['R'] = i
            answer += 'R'
        elif i in (2,5,8,0):
            if i == 0:
                i = 11   
            absL = abs(i - location['L'])
            absR = abs(i - location['R'])
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer+='R'
                location['R'] = i
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer +='L'
                location['L'] = i
            else:
                answer += hand.upper()[:1]
                location[hand.upper()[:1]] = i              
    return answer