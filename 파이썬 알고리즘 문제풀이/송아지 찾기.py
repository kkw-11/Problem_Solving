import sys
from collections import deque
#sys.stdin = open("input.txt","rt")
cnt = 0
dir = [5,-1,1]
def bfs(s,e,visited):
    global cnt
    global dir
    queue = deque()
    queue.append((s,0))
    visited[s] = True

    while queue:
        x, cnt = queue.popleft()
        cnt += 1
        for i in dir:
            nx = x + i
            if nx == e:
                return 
            if nx<0 or nx>10000: continue
            if visited[nx]:continue
            queue.append((nx,cnt))
            visited[nx] = True



s,e = map(int,input().split())
visited = [False]*10001

bfs(s,e,visited)
print(cnt)

#강의 풀이
#from collections import deque

#dir = [-1,1,5]
#def BFS(s,e,visited):
#    queue = deque()
#    queue.append(s)
#    visited[s] = 1 #visited는 방문체크와 동시에 level 체크 현재는 level을 1부터 시작한다고 가정, 그리고 level이 몇번 만에 가는지도 나타내줌

#    while queue:
#        x = queue.popleft()
#        for i in dir:
#            nx = x + i
#            if nx<0 or nx>10000:continue
#            if visited[nx]:continue
#            visited[nx] = visited[x] + 1
             ## nx가 방문도 아직 안했고 문제의 좌표 범위 안에 있다면 아래 문장 수행
#            if nx == e:
#                print(visited[nx]-1) #level을 1부터 시작했기 때문에 1을 빼주고 출력
#                return
#            queue.append(nx)


#visited = [0] * 10001

#s,e = map(int, input().split())

#BFS(s,e,visited)