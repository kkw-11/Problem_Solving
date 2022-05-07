def solution(survey, choices):
    answer = ''
    category = {"R":0,"T":0, "C":0,"F":0, "J":0,"M":0, "A":0,"N":0}
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    indicators = ["RT","CF","JM","AN"]

    n = len(survey)
    # 점수구하기
    for i in range(n):
        if choices[i] == 1 or choices[i] == 2 or choices[i] ==3:
            category[survey[i][0]] += score[choices[i]]
        elif choices[i] == 5 or choices[i] == 6 or choices[i] ==7:
            category[survey[i][1]] += score[choices[i]]
    for indicator1, indicator2 in indicators:
        if category[indicator1] >= category[indicator2]:
            answer += indicator1
        else:
            answer += indicator2




    return answer