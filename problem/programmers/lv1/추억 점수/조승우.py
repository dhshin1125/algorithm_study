def solution(name, yearning, photos):
    name_score = dict()
    answer = []

    for n, y in zip(name, yearning):
        name_score[n] = y

    for photo in photos:
        score = 0
        for p in photo:
            if p in name:
                score += name_score[p]
        answer.append(score)

    return answer우