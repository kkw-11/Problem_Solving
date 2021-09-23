import sys
from collections import deque

def BFS(start):
    global answer

    q = deque()
    visited[start] = True
    q.append(start)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                answer += 1
                q.append(next)
input = sys.stdin.readline
answer = 0
node  = int(input())
edge = int(input())
graph = [[] for _ in range(node+1)]
visited = [False]*(node+1)

for _ in range(edge):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

BFS(1)
print(answer)