# 체육복 부족한 학생 찾아서 해결하는 방법
def solution(n, lost, reserve):
    students = [1]*(n)
    start = 0
    last = n-1

    for l in lost:
        students[l-1] -= 1
    for r in reserve:
        students[r-1] += 1

    for cur in range(n):
        if students[cur] == 0:
            if cur > start and cur < last:
                if students[cur-1] == 2:
                    students[cur-1] -= 1
                    students[cur] += 1
                elif students[cur+1] == 2:
                    students[cur + 1] += 1
                    students[cur] += 1
            elif cur == start:
                if students[cur+1] == 2:
                    students[cur+1] -= 1
                    students[cur] += 1
            elif cur == last:
                if students[cur-1] == 2:
                    students[cur-1] -= 1
                    students[cur] += 1
    lost_cnt = students.count(0)
        
    return n-lost_cnt

# 체육복 여벌있는 학생을 찾아서 해결하는 방법
# def solution(n, lost, reserve):
#     students = [1]*(n)
#     start = 0
#     last = n-1
#     for l in lost:
#         students[l-1] -= 1
#     for r in reserve:
#         students[r-1] += 1

#     for cur in range(n):
#         if students[cur] == 2:
#             if cur > start and cur < last:
#                 if students[cur-1] == 0:
#                     students[cur-1] += 1
#                     students[cur] -= 1
#                 elif students[cur+1] == 0:
#                     students[cur+1] += 1
#                     students[cur] -= 1
#             elif cur == start:
#                 if students[cur+1] == 0:
#                     students[cur+1] += 1
#                     students[cur] -= 1
#             elif cur == last:
#                 if students[cur-1] == 0:
#                     students[cur-1] += 1
#                     students[cur] -= 1
#     lost_cnt = students.count(0)
    
    
        
#     return n-lost_cnt