import sys

def DFS(start,now):
    global answer
    visited[now] = True

    for next in range(n):
        if graph[now][next] :
            answer[start][next] = 1
            if not visited[next]:
                DFS(start,next)

input = sys.stdin.readline

n = int(input())

graph = []
answer = [[0]*n for _ in range(n)]
visited = [False]*n
for _ in range(n):
    a = list(map(int,input().split()))
    graph.append(a)

for i in range(n):
    visited = [False]*n
    DFS(i,i)
for a in answer:
    print(a)
