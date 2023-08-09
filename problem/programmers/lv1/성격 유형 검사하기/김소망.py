def solution(survey, choices):
    answer = ''
    points = {1: 3, 7: 3, 2: 2, 6: 2, 3: 1, 5: 1, 4: 0}
    agree = [7, 6, 5]
    disagree = [1, 2, 3, 4]
    result_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    for i in range(len(survey)):
        if choices[i] in agree:
            result_dict[survey[i][1]] += points[choices[i]]  # agree에 가까운 유형
        else:
            result_dict[survey[i][0]] += points[choices[i]]

    for p in pairs:
        if result_dict[p[0]] >= result_dict[p[1]]:
            answer += p[0]
        else:
            answer += p[1]

    return answer