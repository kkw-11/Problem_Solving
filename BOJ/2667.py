import sys
from collections import deque

sys.stdin = open("input.txt")

def BFS(start_row, start_col, number):
    global cnt
    answer[start_row][start_col] = number
    q = deque()
    q.append((start_row,start_col))

    while q:
       now_row, now_col = q.popleft()

       for dir in range(4):
           next_row = now_row + dir_row[dir]
           next_col = now_col + dir_col[dir]

           if next_row>=0 and next_row<n and next_col>=0 and next_col<n:
               if graph[next_row][next_col] and not answer[next_row][next_col]:
                   answer[next_row][next_col] = number
                   q.append((next_row,next_col))
                   cnt += 1

dir_row = [-1,1,0,0]
dir_col = [0,0,-1,1]
input = sys.stdin.readline

n = int(input())

graph = []
answer = [[0]*n for _ in range(n)]
home_number= 0
result = []
for _ in range(n):
    a = list(map(int,input().rstrip()))
    graph.append(a)

for row in range(n):
    for col in range(n):
        if graph[row][col] and not answer[row][col]:
            home_number += 1
            cnt = 1
            BFS(row,col,home_number)
            result.append(cnt)

print(len(result))
result.sort()
for r in result:
    print(r)