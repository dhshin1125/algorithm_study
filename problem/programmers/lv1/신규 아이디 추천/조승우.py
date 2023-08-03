import re


def solution(new_id):
    # 1단계 lower
    answer = new_id.lower()

    # 2단계
    answer = re.sub(r'[^a-z0-9-_.]', "", answer)

    # 3단계
    answer = re.sub(r'\.{2,}', ".", answer)

    # 4단계
    answer = answer.strip(".")

    # 5단계
    answer = "a" if len(answer) == 0 else answer

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]

    if answer[-1] == ".":
        answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        alpha = answer[-1]
        while (len(answer) < 3): answer += alpha

    return answer