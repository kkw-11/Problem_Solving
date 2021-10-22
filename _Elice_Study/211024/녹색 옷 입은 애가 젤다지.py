import sys
import heapq
from collections import deque

def dijkstra():
    global visited
    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    visited[0][0] = True

    while q:
        now_rupy, now_r,now_c = heapq.heappop(q)

        if now_r == n-1 and now_c == n-1:
            return now_rupy

        for dir in range(4):
            next_r = now_r + dir_r[dir]
            next_c = now_c + dir_c[dir]

            if next_r>=0 and next_r<n and next_c>=0 and next_c<n:
                if not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    heapq.heappush(q,(now_rupy + graph[next_r][next_c],next_r,next_c))


input = sys.stdin.readline
dir_r = [-1,1,0,0]
dir_c = [0,0,-1,1]
cnt = 0
while True:
    cnt += 1
    n = int(input())
    graph = []
    visited = [[False]*n for _ in range(n)]
    if n == 0:
        break
    else:
        for _ in range(n):
            graph.append(list( map(int,input().split())))
        answer = dijkstra()
        print(f"Problem {cnt}: {answer}")