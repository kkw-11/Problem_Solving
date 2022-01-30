def solution(absolutes, signs):
    answer = 0
    
    for index, value in enumerate(signs):
        answer = answer + (absolutes[index] * (1 if value else -1))
    
    return answer