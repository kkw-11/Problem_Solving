import sys
from collections import deque

def BFS(start, end):
    q = deque()
    visited[start] = True
    q.append((start,0))

    while q:
        now, cnt = q.popleft()
        if now == end:
            print(cnt)
            break

        i = 1
        while True:
            next1 = now + stone_bridge[now]*i
            i += 1
            
            if next1>0 and next1<=n:
                if not visited[next1]:
                    visited[next1] = True
                    q.append((next1,cnt+1))
            else:
                break
        
        j = 1
        while True:
            next2 = now - stone_bridge[now]*j
            j += 1

            if next2>0 and next2<=n:
                if not visited[next2]:
                    visited[next2] = True
                    q.append((next2,cnt+1))
            else:
                break
    else:
        print(-1)

input = sys.stdin.readline
n = int(input())

visited = [False]*(n+1)
stone_bridge = [0]

temp = list(map(int,input().split()))
for t in temp:
    stone_bridge.append(t)

start, end = map(int,input().split())

BFS(start,end)