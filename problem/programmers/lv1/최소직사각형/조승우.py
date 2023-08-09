def solution(input):
    x_list = sorted(set(max(i[0], i[1]) for i in input),reverse=True)
    y_list = sorted(set(min(i[0], i[1]) for i in input),reverse=True)
    return x_list[0] * y_list[0]