import sys
from collections import deque

def BFS(start_r,start_c):
    visited[start_r][start_c] = True
    q = deque()
    q.append((start_r,start_c,0))

    while q:
       now_r,now_c,cnt = q.popleft()
       if now_r == end_row and now_c == end_col:
           return cnt

       for dir in range(8):
           next_r = now_r + dir_r[dir]
           next_c = now_c + dir_c[dir]

           if next_r>=0 and next_r<length and next_c>=0 and next_c<length:
               if not visited[next_r][next_c]:
                   visited[next_r][next_c] =True
                   q.append((next_r,next_c,cnt+1))

input = sys.stdin.readline

testcase = int(input())

dir_r = [-1,1,2,2,1,-1,-2,1]
dir_c = [2,2,1,-1,-2,-2,-1,-2]
answer = 0 
for _ in range(testcase):
    length = int(input())
    visited= [[False]*length for _ in range(length)]
    start_row, start_col = map(int,input().split())
    end_row, end_col = map(int, input().split())

    answer = BFS(start_row,start_col)
    print(answer)


