def solution(sizes):
    w = []
    h = []
    for i in sizes:
        i.sort()
        w.append(i[0])
        h.append(i[1])
        
    return max(w) * max(h) 