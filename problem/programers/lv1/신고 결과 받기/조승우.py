def solution(id_list, report, k):
    answer = []

    report_result = {id:set() for id in id_list}
    baned_result = {id:set() for id in id_list}

    # 분리를 할 때 split(구분자)
    for r in report:
        이용자, 신고자 = r.split(" ")
        report_result[이용자].add(신고자)
        baned_result[신고자].add(이용자)

    for id in id_list:
        ret = 0
        for r in report_result[id]:
            if len(baned_result[r]) >= k:
                ret += 1
        answer.append(ret)

    return answer
