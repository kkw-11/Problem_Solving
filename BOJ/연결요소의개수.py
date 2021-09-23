import sys
from collections import deque


def BFS(start):
    global answer
    if not visited[start]:
        answer += 1

    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
input = sys.stdin.readline
answer = 0
node, edge = map(int,input().split())

graph = [[] for _ in range(node+1)]
visited = [False]*(node+1)
for _ in range(edge):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


for start_node in range(1,node+1):
    BFS(start_node)
print(answer)
