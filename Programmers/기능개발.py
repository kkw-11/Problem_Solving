from math import ceil

def solution(progresses, speeds):
    answer = []
    progressesCnt = len(progresses)
    days = []
    newStart = -1
    cnt = 1

    for index, progress in enumerate(progresses):
        days.append(ceil((100 - progress)/speeds[index]))
        
        
    for i in range(progressesCnt):
        if newStart == -1:
            newStart = days[0]
        elif newStart >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            newStart = days[i]
            cnt = 1
    else:
        answer.append(cnt)
        
        
    return answer