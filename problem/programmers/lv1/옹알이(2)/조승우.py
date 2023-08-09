def solution(babbling):
    answer = 0
    pronounce = {"aya", "ye", "woo", "ma"}
    change_char = "9"

    for i in babbling:
        word = i
        for j in pronounce:
            if j*2 not in word:
                word = word.replace(j, change_char * len(j), i.count(j))
                print(word)
        if word.count(change_char) == len(i):
            answer += 1
    return answer