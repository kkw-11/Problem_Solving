from collections import deque
import sys

def go(cur_col,cur_row,region_cnt):
    checked[cur_col][cur_row] = True

    for i in range(4):
        next_col = cur_col + x[i]
        next_row = cur_row + y[i]

        if next_col >=0 and next_col < m and next_row >= 0 and next_row < n:
            if graph[next_col][next_row] == 0 and checked[next_col][next_row] == False:
                region_cnt = go(next_col,next_row,region_cnt+1)

    return region_cnt

input = sys.stdin.readline

m, n, k = map(int,input().split())
answer = []
graph = [[0]*(n) for _ in range(m)]
checked = [[False]*(n) for _ in range(m)]
region_cnt = 0

x = [-1,1,0,0]
y = [0,0,-1,1]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())                   
    for col in range(y1 ,y2):
        for row in range(x1, x2):
            graph[col][row] = 1

for start_col in range(m):
    for start_row in range(n):
        square = 0
            

        if graph[start_col][start_row] == 0 and checked[start_col][start_row] == False:
            region_cnt += 1
            square = go(start_col,start_row,1)
            answer.append(square)

answer.sort()
             
print(region_cnt)
print(*answer)

