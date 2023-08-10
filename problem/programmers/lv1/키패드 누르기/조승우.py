def solution(numbers, hand):
    answer = ''

    pos = {i: ((i - 1) // 3, (i - 1) % 3) for i in range(1, 10)}
    pos["*"] = (3, 0)
    pos[0] = (3, 1)
    pos["#"] = (3, 2)

    left_hand = pos["*"]
    right_hand = pos["#"]

    for n in numbers:
        if n in {1, 4, 7}:
            left_hand = pos[n]
            answer += "L"
        elif n in {3, 6, 9}:
            right_hand = pos[n]
            answer += "R"
        else:
            target = pos[n]

            left_dist = get_distance(target, left_hand)
            right_dist = get_distance(target, right_hand)

            if left_dist > right_dist:
                right_hand = target
                answer += "R"
            elif left_dist < right_dist:
                left_hand = target
                answer += "L"
            else:
                if hand == "right":
                    right_hand = target
                    answer += "R"
                else:
                    left_hand = target
                    answer += "L"
    return answer


def get_distance(target, hand_pos):
    return abs(target[0] - hand_pos[0]) + abs(target[1] - hand_pos[1])