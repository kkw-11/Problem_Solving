import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().rstrip().split())
dfsVisited = [False]*(n+1)
bfsVisited = [False]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

def dfs(vertex):
    dfsVisited[vertex] = True
    print(vertex, end = " ")

    for i in range(1,n+1):
        if graph[vertex][i] == 1 and not dfsVisited[i]:
            dfs(i)

def bfs(start):
    q = deque()
    print(start,end = " ")
    bfsVisited[start] = True
    q.append(start)

    while q:
        curVertex = q.popleft()

        for i in range(1,n+1):
            if graph[curVertex][i] == 1 and not bfsVisited[i]:
                print(i,end = " ")
                q.append(i)
                bfsVisited[i] = True


## 그래프 생성
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1


# dfs
dfs(v)
print("")
# bfs
bfs(v)

