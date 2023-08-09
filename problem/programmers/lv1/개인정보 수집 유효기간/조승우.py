def calculate(today, term, grade, term_day):
    if term_day[grade] < diff_time(today, term):
        return True
    return False


def diff_time(today, term):
    t_y, t_m, t_d = map(int, today.split("."))
    p_y, p_m, p_d = map(int, term.split("."))

    today_days = t_d + (t_m - 1) * 28 + (t_y) * 28 * 12 + 1
    pivot_days = p_d + (p_m - 1) * 28 + (p_y) * 28 * 12

    return today_days - pivot_days


def solution(today, terms, privacies):
    answer = []
    term_day = {i.split(" ")[0]: int(i.split(" ")[1]) * 28 for i in terms}
    for i, v in enumerate(privacies):
        p = v.split(" ")
        if calculate(today, p[0], p[1], term_day):
            answer.append(i + 1)
    return answer