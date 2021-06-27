# https://programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    visited = [False]*n

    def DFS(curVertex,depth):
        if depth == n:
            return
        
        visited[curVertex] = True

        for nextVertex in range(n):
            if visited[nextVertex] == True:
                continue
            if curVertex == nextVertex:
                continue
            if computers[curVertex][nextVertex] == 1:
                DFS(nextVertex,depth+1)

            
    answer = 0
    
    for vertex in range(n):
        if visited[vertex] == False:
            answer +=1
            DFS(vertex,0)
    
    return answer