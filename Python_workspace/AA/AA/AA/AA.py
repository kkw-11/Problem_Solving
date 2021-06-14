#from collections import deque

#dir = [-1,1,5]
#def BFS(s,e,visited):
#    queue = deque()
#    queue.append(s)
#    visited[s] = 1 #visited는 방문체크와 동시에 level 체크 현재는 level을 1부터 시작한다고 가정

#    while queue:
#        x = queue.popleft()
#        for i in dir:
#            nx = x + i
#            if nx<0 or nx>10000:continue
#            if visited[nx]:continue
             ## nx가 방문도 아직 안했고 문제의 좌표 범위 안에 있다면 아래 문장 수행
#            visited[nx] = visited[x] + 1
#            if nx == e:
#                print(visited[nx]-1) #level을 1부터 시작했기 때문에 1을 빼주고 출력
#                return
#            queue.append(nx)


#visited = [0] * 10001

#s,e = map(int, input().split())

#BFS(s,e,visited)