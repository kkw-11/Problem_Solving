import sys
from collections import deque

def go(start, graph, visited):
    global res
    q = deque()
    q.append(start)

    while q:
        parent = q.popleft()
        visited[parent] = True

        for child in graph[parent]:
            if not visited[child]:
                res[child] = parent
                q.append(child)

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
res = [None]*(n+1)


for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

go(1,graph,visited)

for i in range(2,n+1):
    print(res[i])

