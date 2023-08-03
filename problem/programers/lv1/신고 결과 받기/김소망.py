from collections import Counter


def solution(id_list, report, k):
    answer = []
    reporter_dict = {id: set() for id in id_list}
    reported_dict = {id: set() for id in id_list}

    for r in report:
        reporter, reported = r.split(' ')
        reporter_dict[reporter].add(reported)
        reported_dict[reported].add(reporter)

    banned = []
    for v in reporter_dict.values():
        banned.extend(v)
    banned = Counter(banned)

    final_ban = {key for key, value in banned.items() if value >= k}

    for name, value_set in reporter_dict.items():
        answer.append(len(value_set & final_ban))

    return answer