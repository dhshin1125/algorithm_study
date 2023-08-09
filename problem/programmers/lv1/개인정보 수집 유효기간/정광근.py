def todayToday(today):
    year, month, day = map(int, today.split("."))
    return year * 12 * 28 + (month * 28) + day

def solution(today, terms, privacies):
    answer = []
    term_dict = dict()
    days = todayToday(today)
    
    for term in terms:
        term  = term.split()
        term_dict[term[0]] = term[1]
        
    for num, privacie in enumerate(privacies):
        privacie = privacie.split()
        if todayToday(privacie[0]) + int(term_dict[privacie[1]]) * 28 <= days:
            answer.append(num+1)

    return answer