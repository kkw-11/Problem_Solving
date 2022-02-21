import math

def solution(progresses, speeds):
    answer = []
    
    remain_day = []
    distribution = []
    for index, progress in enumerate(progresses):
        remain_day.append(math.ceil((100-progress)/speeds[index]))
    
    for day in remain_day:
        if len(distribution) == 0:
            distribution.append(day)  
        elif len(distribution) != 0 and distribution[0] >= day:
            distribution.append(day)  
        elif len(distribution) != 0 and distribution[0] < day:
            answer.append(len(distribution))
            distribution = []
            distribution.append(day)
            
    if len(distribution):
        answer.append((len(distribution)))
        
    
    return answer