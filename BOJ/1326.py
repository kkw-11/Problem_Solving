import sys
from collections import deque

def BFS(start, end):
    q = deque()
    checked[start] = True
    q.append((start,0))

    while q:
        now, cnt = q.popleft()
        if now == end:
            print(cnt)
            break

        i = 0
        while True:
            i += 1
            next1 = now + stone_bridge[now]*i
            
            if next1>0 and next1<=n:
                if not checked[next1]:
                    checked[next1] = True
                    q.append((next1,cnt+1))
            else:
                break
        
        j = 0
        while True:
            j += 1
            next2 = now - stone_bridge[now]*j

            if next2>0 and next2<=n:
                if not checked[next2]:
                    checked[next2] = True
                    q.append((next2,cnt+1))
            else:
                break
    else:
        print(-1)

input = sys.stdin.readline
n = int(input())

checked = [False]*(n+1)
stone_bridge = [0]

temp = list(map(int,input().split()))
for t in temp:
    stone_bridge.append(t)

start, end = map(int,input().split())

BFS(start,end)