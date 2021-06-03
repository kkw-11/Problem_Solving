
import sys 
from collections import deque
#sys.stdin = open("input.txt","rt")

cnt = 0
def DFS(graph, ch, vertex,flag):
    if ch[vertex] == 1:
        return

    ch[vertex] = 1
    global cnt
    if flag == 1:
        for i in range(1,n+1):
            if graph[vertex][i] == 1 and ch[i] != 1:
                cnt += 1
                DFS(graph,ch,i,flag)
    elif flag == -1:
        for i in range(1,n+1):
            if graph[vertex][i] == -1 and ch[i] != 1:
                cnt += 1
                DFS(graph,ch,i,flag)

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
        DFS(graph,ch,i,1)
        
        for j in range(1,n+1):
            ch[j]= 0
        DFS(graph,ch,i,-1)

        if cnt == n-1:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

answer = solution(n,results)

print(answer)

