import sys
from collections import deque

#sys.stdin = open("input.txt","rt")

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def BFS(y,x,graph,answer):
    q = deque()

    q.append((y,x))

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            if answer[ny][nx] > graph[ny][nx] + answer[curY][curX]:
                answer[ny][nx] = graph[ny][nx] + answer[curY][curX]
                q.append((ny,nx))

count = 1
while True:
    graph = []
    n = int(input())
    if n == 0:
        break
    
    answer = [[99999] * n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    answer[0][0] = graph[0][0]

    BFS(0,0,graph,answer)
    print(f"Problem {count}: {answer[n-1][n-1]}")
    count += 1
