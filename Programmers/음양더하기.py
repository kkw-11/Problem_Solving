def solution(absolutes, signs):
    answer = 0
    
    for index, value in enumerate(absolutes):
        if signs[index]:
            answer += absolutes[index]
        else:
            answer -= absolutes[index]
    
    return answer