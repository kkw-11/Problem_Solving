from math import ceil

def solution(progresses, speeds):
    answer = []
    remaining_days = []
    q = []
    
    for index, progress in enumerate(progresses):
        remaining_days.append(ceil((100 - progress)/speeds[index]))


    for remaining_day in remaining_days:
        if len(q) == 0:
            q.append(remaining_day)
        elif len(q) > 0 and q[0] >= remaining_day:
            q.append(remaining_day)
        else:
            answer.append(len(q))
            q = []
            q.append(remaining_day)
    else:
        answer.append(len(q))
            
    return answer