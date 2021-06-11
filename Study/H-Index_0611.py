#https://programmers.co.kr/learn/courses/30/lessons/42747



#선형 탐색
# def linearSolution(citations):
#     answer = 0 
#     n = len(citations)
#     citations.sort()
    

#     for idx, value in enumerate(citations):
#         if (n-idx) >= value: # n-idx : value 이상 인용된 논문수
#             answer = value
#         else:
#             break

#     return answer
    
def binarySolution(citations):
    answer = 0 
    n = len(citations)
    citations.sort()
    rIdx = n-1
    lIdx = 0   
    midIdx = (rIdx+lIdx)//2
     
    while rIdx-lIdx>=10:
        midIdx = (rIdx+lIdx)//2
        if n - midIdx>=citations[midIdx]:
            lIdx = midIdx
        else:
            rIdx = midIdx

    for idx in range(lIdx,rIdx+1):
        if (n-idx) >= citations[idx]: # n-idx : value 이상 인용된 논문수
            answer = citations[idx]
        else:
            break

    return answer


citations = [3, 0, 6, 1, 5]

print(binarySolution(citations))

