def solution(n, lost, reserve):
    answer = 0
    students = [1]*(n)
    
    for l in lost:
        students[l-1] -= 1
    for r in reserve:
        students[r-1] += 1

    for cur in range(n):
        if students[cur] == 0:
            if cur > 0 and cur < n-1:
                if students[cur-1] == 2:
                    students[cur-1] -= 1
                    students[cur] += 1
                elif students[cur+1] == 2:
                    students[cur + 1] += 1
                    students[cur] += 1
            elif cur == 0:
                if students[cur+1] == 2:
                    students[cur+1] -= 1
                    students[cur] += 1
            elif cur == n-1:
                if students[cur-1] == 2:
                    students[cur-1] -= 1
                    students[cur] += 1
    lost_cnt = students.count(0)
    
    
        
    return n-lost_cnt