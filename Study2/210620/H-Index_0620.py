#https://programmers.co.kr/learn/courses/30/lessons/42747


def solution(citations):
    answer = 0 
    citations.sort()  
    # value[0, 2, 4,40,41,42,43,44] 2번 이상 인용된 논문이 7편
    # len(citations[idx:][8, 7, 6, 5, 4, 3, 2, 1]
    # [3, 0, 6, 1, 5]
    
    # [0,1,3,5,6]
    # [5,4,3,2,1]

    for idx, h in enumerate(citations):
        if h >= len(citations[idx:]): # h:논문 인용 횟수, len(citations[idx:]):h이상 논문 편수
            answer = len(citations[idx:])
            return answer
    return answer
        


#선형 탐색
# def solution(citations):
#     answer = 0 
#     n = len(citations)
#     citations.sort()
    

#     for idx, value in enumerate(citations):
#         if (n-idx) >= value: # n-idx : value 이상 인용된 논문수
#             answer = value
#         else:
#             break

#     return answer
    
# def binarySolution(citations):
#     answer = 0 
#     n = len(citations)
#     citations.sort()
#     rIdx = n-1
#     lIdx = 0   
#     midIdx = (rIdx+lIdx)//2
     
#     while rIdx-lIdx>=10:
#         midIdx = (rIdx+lIdx)//2
#         if n - midIdx>=citations[midIdx]:
#             lIdx = midIdx
#         else:
#             rIdx = midIdx

#     for idx, value in enumerate(citations): 
#         if value >= len(citations[idx:]):  #[0,1,3,5,6]
#             answer = len(citations[idx:])
#             return answer

#     return answer


# citations = [3, 0, 6, 1, 5]

# print(binarySolution(citations))

