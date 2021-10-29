import sys
from collections import deque

def BFS(start_row, start_col, rain):
    global safe_area

    q = deque()
    q.append((start_row,start_col))
    safe_area[row][col] = True

    while q:
        now_row, now_col = q.popleft()

        for dir in range(4):
            next_row = now_row + dir_row[dir]
            next_col = now_col + dir_col[dir]
            if next_row >= 0 and next_row<n and next_col>=0 and next_col<n:
                if not safe_area[next_row][next_col]:
                    if graph[next_row][next_col] > rain:
                        safe_area[next_row][next_col] = True
                        q.append((next_row, next_col))

input = sys.stdin.readline

n = int(input())

max_height = float("-inf")
graph = []
dir_row = [-1,1,0,0]
dir_col = [0,0,-1,1]
max_safe_cnt = -1

for _ in range(n):
    a = list(map(int, input().split()))
    a_max = max(a)
    if max_height < a_max:
        max_height = a_max
    graph.append(a)

for rain in range(max_height):
    safe_area = [[False]*n for _ in range(n)]
    safe_cnt = 0 
    for row in range(n):
        for col in range(n):
            if graph[row][col] > rain and not safe_area[row][col]:
                safe_cnt += 1
                BFS(row,col, rain)
    if max_safe_cnt <safe_cnt:
        max_safe_cnt = safe_cnt
print(max_safe_cnt)