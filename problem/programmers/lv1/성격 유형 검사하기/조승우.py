def solution(survey, choices):
    answer = ''
    personal_type = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for idx, value in enumerate(survey):
        score = choices[idx] - 4
        if -3 <= score <= -1:
            personal_type[value[0]] += (-score)
        elif 1 <= score <= 3:
            personal_type[value[1]] += score

    keys = list(personal_type.keys())
    for i in range(len(personal_type.keys())//2):
        first, second = keys[i * 2], keys[i * 2 + 1]
        if personal_type[first] >= personal_type[second]:
            answer += first
        else:
            answer += second

    return answer우