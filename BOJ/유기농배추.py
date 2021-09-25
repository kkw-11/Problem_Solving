import sys
from collections import deque

def BFS(cur_row, cur_col):
    visited[cur_row][cur_col] = True
    q = deque()
    q.append((cur_row,cur_col))

    while q:
        now_row, now_col = q.popleft()

        for i in range(4):
            next_row = now_row + dir_row[i]
            next_col = now_col + dir_col[i]

            if next_row>=0 and next_row<row and next_col>=0 and next_col<col:
                if not visited[next_row][next_col] and graph[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row,next_col))

input = sys.stdin.readline

testcase = int(input())
dir_row = [-1,1,0,0]
dir_col = [0,0,-1,1]

for _ in range(testcase):
    col, row, edge = map(int,input().split())
    graph = [[0]*(col) for _ in range(row)]
    visited = [[False]*(col) for _ in range(row)]

    for _ in range(edge):
        a, b = map(int,input().split())
        graph[b][a] = 1
    answer = 0 
    for i in range(row):
        for j in range(col):
            if graph[i][j]:
                if not visited[i][j]:
                    answer += 1
                    BFS(i,j)

    print(answer)