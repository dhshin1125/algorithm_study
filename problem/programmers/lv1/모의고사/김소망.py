def solution(answers):
    answer_cnt = {i: 0 for i in range(1, 4)}
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(len(answers)):
        if answers[i] == students[0][i % (len(students[0]))]:
            answer_cnt[1] += 1
        if answers[i] == students[1][i % (len(students[1]))]:
            answer_cnt[2] += 1
        if answers[i] == students[2][i % (len(students[2]))]:
            answer_cnt[3] += 1

    answer = []
    for k, v in answer_cnt.copy().items():
        if v == max(answer_cnt.values()):
            answer.append(k)
    return answer