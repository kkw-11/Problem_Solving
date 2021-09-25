import sys
from collections import deque

sys.stdin = open("input.txt")

def BFS(start_row, start_col):
    visited[start_row][start_col] = True
    q= deque()
    q.append((start_row,start_col))

    while q:
        now_row, now_col = q.popleft()

        for dir in range(4):
            next_row = now_row + dir_row[dir]
            next_col = now_col + dir_col[dir]

            if next_row>=0 and next_row<field_row and next_col>=0 and next_col<field_col:
                if not visited[next_row][next_col] and field[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row,next_col))

input = sys.stdin.readline

dir_row = [-1,1,0,0]
dir_col = [0,0,-1,1]
testcast = int(input())

for _ in range(testcast):
    field_col, field_row, number_of_position = map(int,input().split())

    visited = [[False]*(field_col) for _ in range(field_row)]
    field = [[0]*(field_col) for _ in range(field_row)]
    answer = 0

    for _ in range(number_of_position):
        col, row = map(int, input().split())
        field[row][col] = 1
    
    for i in range(field_row):
        for j in range(field_col):
            if field[i][j] and not visited[i][j]:
                answer += 1
                BFS(i,j)
    print(answer)