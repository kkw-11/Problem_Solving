import sys
from collections import deque

def BFS():
    global answer, check

    q = deque()

    for tomato in tomatoes:
        q.append(tomato)
        checked[tomato[0]][tomato[1]] = True
    
        
    while q:
        now_r, now_c, now_day = q.popleft()

        if answer < now_day:
            answer = now_day

        for dir in range(4):
            next_r = now_r + dir_r[dir]
            next_c = now_c + dir_c[dir]
            if next_r>=0 and next_r<row and next_c>=0 and next_c<col:
                if not checked[next_r][next_c] and graph[next_r][next_c] == 0:
                    check +=1
                    q.append((next_r,next_c,now_day+1))
                    checked[next_r][next_c] = True


input = sys.stdin.readline

answer = 0
check = 0
cnt = 0
graph = []
tomatoes = []
dir_r = [-1,1,0,0]
dir_c = [0,0,-1,1]

col, row = map(int,input().split())
checked = [[False]*col for _ in range(row)]

for i in range(row):
    a = list(map(int,input().split()))
    graph.append(a)

for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            tomatoes.append((i,j,0))
        elif graph[i][j] == 0:
            cnt += 1
BFS()

if check < cnt:
    print(-1)
elif check == cnt:
    print(answer)