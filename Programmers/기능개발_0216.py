from math import ceil

def solution(progresses, speeds):
    answer = []
    remaining_days = []
    distributions = []
    
    for index, progress in enumerate(progresses):
        remaining_days.append(ceil((100 - progress)/speeds[index]))


    for remaining_day in remaining_days:
        if len(distributions) == 0:
            distributions.append(remaining_day)
        elif len(distributions) > 0 and distributions[0] >= remaining_day:
            distributions.append(remaining_day)
        else:
            answer.append(len(distributions))
            distributions = []
            distributions.append(remaining_day)
    else:
        answer.append(len(distributions))
            
    return answer