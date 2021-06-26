# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    visited = [False]*n

    def DFS(i,depth):
        if depth == n:
            return
        
        visited[i] = True

        for j in range(n):
            if visited[j] == True:
                continue
            if i == j:
                continue
            if computers[i][j] == 1:
                DFS(j,depth+1)

            
    answer = 0
    
    for i in range(n):
        if visited[i] == False:
            answer +=1
            DFS(i,0)
    
    return answer