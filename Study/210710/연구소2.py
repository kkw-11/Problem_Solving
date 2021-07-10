# https://www.acmicpc.net/problem/17141
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global q, c, ans
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and c[nx][ny] == -1:
                if a[nx][ny] == 0:
                    c[nx][ny] = c[x][y] + 1
                    cnt = max(cnt, c[nx][ny])
                    q.append([nx, ny])

    for i in range(n):
        for j in range(n):
            if a[i][j] == 0 and c[i][j] == -1:
                cnt = sys.maxsize
    ans = min(ans, cnt)

def dfs(index, cnt):
    global q, c, ans
    if cnt == m:
        q = deque()
        c = [[-1]*n for _ in range(n)]
        for i in range(len(virus)):
            if select[i]:
                q.append([virus[i][0], virus[i][1]])
                c[virus[i][0]][virus[i][1]] = 0
        bfs()
        return

    for i in range(index, len(virus)):
        if select[i]:
            continue
        select[i] = 1
        dfs(i+1, cnt+1)
        select[i] = 0

n, m = map(int, input().split())

a, virus = [], []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for j in range(n):
        if a[i][j] == 2:
            virus.append([i, j])
            a[i][j] = 0

select = [0 for _ in range(10)]
ans = sys.maxsize
dfs(0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)