import numpy as np


def solution(numbers, hand):
    answer = ''
    phone = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [98, 0, 99]])
    left = phone[:, 0]
    right = phone[:, -1]
    x_l, y_l, x_r, y_r = 3, 0, 3, 2  # * # 위치

    for n in numbers:
        if n in left:
            L = np.argwhere(phone == n)[0]  # 왼손으로 이동한 위치 기록
            x_l, y_l = L[0], L[1]
            answer += 'L'
        elif n in right:
            R = np.argwhere(phone == n)[0]  # 오른손으로 이동한 위치 기록
            x_r, y_r = R[0], R[1]
            answer += 'R'
        else:
            M = np.argwhere(phone == n)[0]
            x_m, y_m = M[0], M[1]
            dl = abs(x_m - x_l) + abs(y_m - y_l)
            dr = abs(x_m - x_r) + abs(y_m - y_r)

            if dl > dr:  # R이 더 가까우면
                R = np.argwhere(phone == n)[0]
                x_r, y_r = R[0], R[1]
                answer += 'R'
            elif dr > dl:
                L = np.argwhere(phone == n)[0]
                x_l, y_l = L[0], L[1]
                answer += 'L'
            else:
                if hand == "right":
                    R = np.argwhere(phone == n)[0]
                    x_r, y_r = R[0], R[1]
                    answer += 'R'
                else:
                    L = np.argwhere(phone == n)[0]
                    x_l, y_l = L[0], L[1]
                    answer += 'L'

    return answer
