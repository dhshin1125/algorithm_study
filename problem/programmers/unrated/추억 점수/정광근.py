def solution(name, yearning, photo):
    name_dict = {id:score for score, id in zip(yearning,name)}
    answer = []
    for pho in photo:
        count = 0
        for ph in pho:
            if ph in name_dict:
                count += name_dict[ph]
        answer.append(count)
    return answer