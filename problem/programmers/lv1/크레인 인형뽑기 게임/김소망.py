import numpy as np


def solution(board, moves):
    answer = 0
    basket = []
    board = np.array(board)

    for m in moves:
        idx = m - 1
        column = list(board[:, idx])
        item = next(([i, num] for i, num in enumerate(column) if num != 0), None)
        if item != None:
            basket.append(item[1])
            board[:, idx][item[0]] = 0
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer