#https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
# import sys 
#sys.stdin = open("input.txt","rt")
#인접행렬 방식으로 그래프 표현
cnt = 0
def DFS(graph, visited, vertex,flag,n):
    visited[vertex] = 1
    global cnt
    if flag == 1:
        for i in range(1,n+1):
            if graph[vertex][i] == 1 and visited[i] != 1:
                cnt += 1
                DFS(graph,visited,i,flag,n)
    elif flag == -1:
        for i in range(1,n+1):
            if graph[vertex][i] == -1 and visited[i] != 1:
                cnt += 1
                DFS(graph,visited,i,flag,n)

    return 

def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]
    ch = [0]*(n+1)
    global cnt

    # 입력 값으로 그래프 만들기
    for result in results:
        graph[result[0]][result[1]] = 1
        graph[result[1]][result[0]] = -1

    for i in range(1,n+1):
        for j in range(1,n+1):
            ch[j]= 0
        cnt = 0
        # 승 수 계산
        DFS(graph,ch,i,1,n)

        for j in range(1,n+1):
            ch[j]= 0
        # 패 수 계산
        DFS(graph,ch,i,-1,n)

        # 승수와 패수를 모두 계산한
        if cnt == n-1:
            answer += 1

    return answer