def solution(s):
    dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    keys = dict.keys()

    for i in keys:
        s = s.replace(i, dict[i])

    return int(s)