from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}

    idx = 1
    today = datetime.strptime(today, '%Y.%m.%d')
    for t in terms:
        k, v = t.split(' ')
        terms_dict[k] = v

    for p in privacies:
        date, term = p.split(' ')
        dd = datetime.strptime(date, '%Y.%m.%d')
        contract = terms_dict[term]
        diff = relativedelta(today, dd)
        diff_months = diff.years * 12 + diff.months
        if diff_months >= int(contract):
            answer.append(idx)
        idx += 1

    return answer