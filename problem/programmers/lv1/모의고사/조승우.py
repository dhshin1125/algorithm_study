def solution(input):
    num1 = [i for i in ("1,2,3,4,5,"* 2000).split(",")]
    num2 = [i for i in ("2,1,2,3,2,4,2,5,"* 1250).split(",")]
    num3 = [i for i in ("3,3,1,1,2,2,4,4,5,5,"* 1000).split(",")]

    num1_score = sum([1 for idx, val in enumerate(input) if num1[idx] == str(val)])
    num2_score = sum([1 for idx, val in enumerate(input) if num2[idx] == str(val)])
    num3_score = sum([1 for idx, val in enumerate(input) if num3[idx] == str(val)])

    max_score = max(num1_score, num2_score, num3_score)

    return [idx+1 for idx,val in enumerate([num1_score, num2_score, num3_score]) if val == max_score]