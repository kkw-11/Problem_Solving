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