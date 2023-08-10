from collections import deque

def solution(cards1, cards2, goal):
    c1, c2 = 0, 0
    g = deque(goal)

    while g:
        t = g.popleft()

        if cards1[c1] == t and c1 < len(cards1) - 1:
            c1 += 1
            continue
        if cards2[c2] == t and c2 < len(cards2) - 1:
            c2 += 1
            continue

        if t not in (cards2[c2], cards1[c1]):
            return "No"
    return "Yes"
