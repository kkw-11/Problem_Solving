def solution(dartResult):
    answer = 0
    scores = [None]*3
    BONUS = ["S","D","T"]
    OPTION = ["*","#"]
    
    dart_round = 0
    for score in dartResult:
        if score in "0123456789":
            if scores[dart_round] == None:
                scores[dart_round] = int(score)
            else:# 점수 10점 계산하기 위한 코드
                scores[dart_round] = scores[dart_round]*10 + int(score)
        if score in BONUS:
            if score == BONUS[1]:
                scores[dart_round] = scores[dart_round]**2
            if score == BONUS[2]:
                scores[dart_round] = scores[dart_round]**3
            dart_round += 1

        if score in OPTION:
            if dart_round-1 != 0 and score == OPTION[0]:
                scores[dart_round-1] = scores[dart_round-1]*2
                scores[dart_round-2] = scores[dart_round-2]*2
            elif dart_round-1 == 0 and score == OPTION[0]:
                scores[dart_round-1] = scores[dart_round-1]*2

            if score == OPTION[1]:
                scores[dart_round-1] = -scores[dart_round-1]

    answer = sum(scores)
    return answer