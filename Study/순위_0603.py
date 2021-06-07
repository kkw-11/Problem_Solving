#https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

import sys 
from collections import deque
#sys.stdin = open("input.txt","rt")

cnt = 0
def DFS(graph, visited, vertex,flag,n):
    if visited[vertex] == 1:
        return

    visited[vertex] = 1
    global cnt
    # 승 방향 그래프 탐색
    if flag == 1:
        for i in range(1,n+1):
            if graph[vertex][i] == 1 and visited[i] != 1:
                cnt += 1
                DFS(graph,visited,i,flag,n)
    # 패 방향 그래프 탐색
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

        if cnt == n-1:
            answer += 1

    return answer