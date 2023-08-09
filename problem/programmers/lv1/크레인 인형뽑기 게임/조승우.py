def solution(board, moves):
    # 정답
    answer = 0

    # 크레인의 각각의 슬롯들 선언
    slot = list(list() for _ in range(len(board)))

    # 크레인의 각각의 슬롯들에 board 의 입력값들을 담음
    # 0인 경우는 빈 공간이기에 0을 제외한 나머지 값들을 후입선출 방식으로 만들기
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board)):
            if board[i][j] != 0:
                slot[j].append(board[i][j])
    # 인형의 퇴출구
    ret = list()

    # 크레인의 움직임들
    for m in moves:
        # 만약 인형이 있는 슬롯에서만 정상적으로 동작해야 함
        if len(slot[m - 1]) > 0:
            ret.append(slot[m - 1].pop())
            print(ret)
            # 인형 슬롯에 2개 이상일 때 2개씩 짝이 맞는지 체크
            # 짝이 맞을 경우, 두 개 제거
            if len(ret) >= 2 and ret[-1] == ret[-2]:
                ret.pop()
                ret.pop()
                answer += 2
    return answer우