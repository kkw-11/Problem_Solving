import sys
from collections import deque

def BFS():
    global answer
    
    q = deque()

    visited[1] = True
    q.append((1,0))

    while q:
        friend, count = q.popleft()

        if 1<= count <=2 :
            answer += 1
        if count > 3:
            break

        for next_friend in graph[friend]:
            if not visited[next_friend]:
                visited[next_friend] = True
                q.append((next_friend, count+1))

input = sys.stdin.readline
answer = 0
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
BFS()

print(answer)