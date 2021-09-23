import sys
from collections import deque

input = sys.stdin.readline

subin, brother = map(int, input().split())
visited = [False]*(100001)
q = deque()

q.append((subin,0))

while q:
    cur, time = q.popleft()

    if cur == brother:
        print(time)
        break

    for move in [-1,1,cur]:
        next = cur + move
        if 0<= next <= 100000 and not visited[next]:
            visited[next] = True
            q.append((next,time+1))