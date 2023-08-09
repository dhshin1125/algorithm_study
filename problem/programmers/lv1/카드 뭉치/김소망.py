def solution(cards1, cards2, goal):
    answer = ''
    cards1, cards2, goal = cards1[::-1], cards2[::-1], goal[::-1]

    for _ in range(len(goal)):
        if cards1 and goal[-1] == cards1[-1]:
            goal.pop()
            cards1.pop()
        elif cards2 and goal[-1] == cards2[-1]:
            goal.pop()
            cards2.pop()

    if not goal: return 'Yes'
    else: return 'No'