#https://programmers.co.kr/learn/courses/30/lessons/43165

res = 0

def DFS(numbers,depth,targetNum,total):
    if depth == len(numbers):
        if total == targetNum:
            global res
            res += 1
        return
            
    total += numbers[depth]
    DFS(numbers,depth+1,targetNum,total)
    total -= numbers[depth]
    
    total -= numbers[depth]
    DFS(numbers,depth+1,targetNum,total)
    total += numbers[depth]
    
    

def solution(numbers, target):
    answer = 0 
    
    DFS(numbers,0,target,0)
    
    answer = res
    
    return answer

# from collections import deque

# def solution(numbers, target):
#     answer = 0
#     queue = deque()

#     n = len(numbers) #[1,1,1,1,1]
#     queue.append([numbers[0], 0])
#     queue.append([-1*numbers[0], 0])

#     while queue:
#         temp, idx = queue.popleft() 
#         idx += 1
#         if idx < n:
#             queue.append([temp+numbers[idx], idx])
#             queue.append([temp-numbers[idx], idx])
#         else:
#             if temp == target:
#                 answer += 1
#     return answer

# numbers=[1,1,1,1,1]
# print(solution(numbers,3))

