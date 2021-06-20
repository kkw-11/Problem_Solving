#https://programmers.co.kr/learn/courses/30/lessons/42586
import math
def solution(progresses, speeds):
    answer = []
    progressesCnt = len(progresses)
    days = [100]*progressesCnt
    for i in range(progressesCnt):    
        days[i] = math.ceil((100 - progresses[i])/speeds[i])
        
        
    newStart = days[0]
    cnt = 1
    for i in range(1,progressesCnt):
        if newStart >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            newStart = days[i]
            cnt = 1
    else:
        answer.append(cnt)
        
        
    return answer