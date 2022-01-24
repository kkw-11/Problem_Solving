def solution(absolutes, signs):
    answer = 0
    
    for index, value in enumerate(signs):
        answer += absolutes[index]  if value else answer -= absolutes[index]
    
    return answer