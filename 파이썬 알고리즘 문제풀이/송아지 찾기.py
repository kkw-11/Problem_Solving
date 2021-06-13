import sys
from collections import deque
#sys.stdin = open("input.txt","rt")
cnt = 0
dir = [5,-1,1]
def bfs(s,e,visited):
    global cnt
    global dir
    queue = deque()
    queue.append((s,0))
    visited[s] = True

    while queue:
        x, cnt = queue.popleft()
        cnt += 1
        for i in dir:
            nx = x + i
            if nx == e:
                return 
            if nx<0 or nx>10000: continue
            if visited[nx]:continue
            queue.append((nx,cnt))
            visited[nx] = True



s,e = map(int,input().split())
visited = [False]*10001

bfs(s,e,visited)
print(cnt)