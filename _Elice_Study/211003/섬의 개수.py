import sys
from collections import deque

input = sys.stdin.readline

def BFS(start_r, start_c):

    q = deque()

    visited[start_r][start_c] = True
    q.append((start_r,start_c))

    while q:
        now_r, now_c = q.popleft()

        for dir in range(8):
            next_r = now_r + dir_r[dir]
            next_c = now_c + dir_c[dir]

            if next_r>=0 and next_r<row and next_c>=0 and next_c<col:
                if graph[next_r][next_c] and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    q.append((next_r,next_c))

dir_r = [-1,1,0,0,1,-1,1,-1]
dir_c = [0,0,-1,1,1,1,-1,-1]
while True:
    col, row = map(int,input().split())
    if col == 0 and row == 0:
        break
    else:
        visited = [[False]*col for _ in range(row)]
        graph = []
        cnt = 0
        for _ in range(row):
            graph.append(list(map(int,input().split())))
        for r in range(row):
            for c in range(col):
                if graph[r][c] and not visited[r][c]:
                    cnt += 1
                    BFS(r,c)
        print(cnt)