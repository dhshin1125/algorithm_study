from collections import Counter


def solution(name, yearning, photo):
    answer = []
    points = {}
    for i in range(len(name)):
        points[name[i]] = yearning[i]

    for p in photo:
        total = 0
        temp = Counter(p)

        for k, v in temp.items():
            if k in points.keys():
                total += points[k] * v
        answer.append(total)

    return answer