import sys
from collections import deque

def BFS(start):
    global answer
    
    q = deque()
    visited[start-1] = True
    q.append(start)
    answer += 1
    
    while q:
        now = q.popleft()

        for move in (stone[now-1],-stone[now-1]):
            next = now + move
            
            if next>0 and next<=n and not visited[next-1]:
                visited[next-1] = True
                q.append(next)
                answer += 1

input = sys.stdin.readline
n = int(input())
visited = [False]*(n)
stone = list(map(int,input().split()))
start = int(input())
answer = 0

BFS(start)
print(answer)