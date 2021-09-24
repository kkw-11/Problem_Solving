import sys

input = sys.stdin.readline

people = int(input())

a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(people+1)]
visited = [False]*(people+1)
answer = -1
flag = False

for _ in range(m):
    parent, child = map(int,input().split()) 
    graph[parent].append(child)
    graph[child].append(parent)

def find(person,relation):
    global answer, flag
    visited[person] = True
    if person == b:
        print(relation)
        flag = True
        return
    for p in graph[person]:
        if not visited[p]:
            find(p, relation+1)
find(a,0)
if not flag:
    print(-1)

#from collections import deque
#import sys

#def bfs(row, col):
#    global visited, safe_length
#    pre_length = 0
#    q = deque()

#    q.append((row,col,0))
#    visited[row][col] = True
#    if shark_map[row][col] == 1:
#        safe_length[row][col] = 0
#        return

#    while q:
#        pre_row, pre_col, pre_length = q.popleft()

#        for i in range(8):
#            next_row = pre_row + dir_row[i]
#            next_col = pre_col + dir_col[i]

#            if next_row >= 0 and next_row <n and next_col>=0 and next_col < m:
#                if shark_map[next_row][next_col] == 1:
#                    safe_length[row][col] = pre_length + 1
#                    return

#                if not visited[next_row][next_col]:
#                    visited[next_row][next_col] = True
#                    q.append((next_row,next_col,pre_length+1))

#sys.stdin = open("input.txt")
#input = sys.stdin.readline

#n,m = map(int,input().split())

#answer = -99999999
#shark_map = []
#safe_length = [[0]*m for _ in range(n)]
#visited = [[False]*m for _ in  range(n)]
#dir_row = [0,1,1,1,0,-1,-1,1]
#dir_col = [1,1,0,-1,-1,-1,0,1]

#for _ in range(n):
#    input_data = list(map(int, input().split()))
#    shark_map.append(input_data)

#for row in range(n):
#    for col in range(m):
#        bfs(row,col)
#        visited = [[False]*m for _ in  range(n)]

#        if answer < safe_length[row][col]:
#            answer = safe_length[row][col]

#print(safe_length)
#print()
#print(answer)


#import sys
#from collections import deque

#def bfs_print():
#    q= deque()
#    visited[1] = True
#    q.append((1,0))

#    while q:
#        node, length = q.popleft()

#        if answer[node] == -1 or answer[node] > length:
#            answer[node] = length

#        for next_node in graph[node]:
#            if not visited[next_node]:
#                visited[next_node] = True
#                q.append((next_node, length+1))
#    for i in range(1,city+1):
#        print(answer[i], end = " ")
#    print()

                
#sys.stdin = open("input.txt")
#input = sys.stdin.readline

#city, street = map(int,input().split())

#graph = [[] for _ in range(city+1)]
#visited = [False] * (city+1)
#answer = [-1]*(city+1)

#for _ in range(street):
#    city1, city2 = map(int,input().split())
#    graph[city1].append(city2)

#qstreet = int(input())
#for _ in range(qstreet):
#    city1, city2 = map(int,input().split())
#    graph[city1].append(city2)
#    visited = [False] * (city+1)
#    bfs_print()



#x = 20
#def foo():
#    x = 10

#    return x


#x = foo()
#print(x)


#def foo():
#    global x
#    x = 10
#    print(x)


#foo()
#print(x)
#def A():
#    x = 10

#    def B():
#        x = 20
#        return x

#    x = B()
#    print(x)

#A()


#def A():
#    x = 10

#    def B():
#        nonlocal x
#        x = 20

#    B()
#    print(x)

#A()


##def A():
#    x = 10

#    def B():
#        x = 20

#    B()
#    print(x)

#A()


#def foo():
#    global x 
#    x= 10

#foo()
#print(x)

#def foo():
#    global x
#    x = 3
#    print(x)
#    print(graph)

#x = 10
#print(x)
#graph = [1,2,3]
#foo()
#print(x)


#def foo():
#    x = 3
#    graph = [22,2332]
#    print(x)
#    print(graph)

#x = 10
#graph = [1,2,3]
#foo()
#print(x)



#def foo():
#    print(x)
#    print(graph)

#x = 10
#graph = [1,2,3]
#foo()



#x= 10

#def foo():

#    print(x)
#foo()

#print(x)




## 음의 경로가 없는 그래프에서 특정 출발노드에서 다른 모든 노드로 가는 최단경로 알고리즘
## 음의 간선이 없는 현실세계에서 최단경로를 구할 때 사용
## 매 상황에서 비용이 적은 그리디 기법으로 최단경로를 구하는 방법, 그리디로 최단경로로 이동하다가 새로운 최단경로 값이 나오면 갱신

## 동작과정
### 출발노드 설정
### 최단거리 테이블 초기화
### 방문하지 않은 노드 중에서 ㅗ치단 거리가 가장 짧으 노드를 선택
### 해당 노드를 거쳐 다른 노드로 가는 비용 계산하여 최단 거리 테이블을 갱신
### 모든 노드 방문할때까지 3번과 4번 반복

#import sys

#sys.stdin = open("input.txt")
#input = sys.stdin.readline
#INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

## 노드의 개수, 간선의 개수를 입력받기
#n = int(input())
#m = int(input())
## 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
#graph = [[] for i in range(n + 1)]
## 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
#visited = [False] * (n + 1)
## 최단 거리 테이블을 모두 무한으로 초기화
#distance = [INF] * (n + 1)

## 모든 간선 정보를 입력받기
#for _ in range(m):
#    a, b, c = map(int, input().split())
#    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#    graph[a].append((b, c))

## 시작 노드 번호를 입력받기
#start, end = map(int, input().split())

## 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
#def get_smallest_node():
#    min_value = INF
#    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
#    for i in range(1, n + 1):
#        if distance[i] < min_value and not visited[i]:
#            min_value = distance[i]
#            index = i
#    return index

#def dijkstra(start):
#    # 시작 노드에 대해서 초기화
#    distance[start] = 0
#    visited[start] = True
#    for j in graph[start]:
#        distance[j[0]] = j[1]
#    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
#    for i in range(n - 1):
#        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
#        now = get_smallest_node()
#        visited[now] = True
#        # 현재 노드와 연결된 다른 노드를 확인
#        for j in graph[now]:
#            cost = distance[now] + j[1]
#            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#            if cost < distance[j[0]]:
#                distance[j[0]] = cost

## 다익스트라 알고리즘을 수행
#dijkstra(start)
#print(distance[end])


# 모든 노드로 가기 위한 최단 거리를 출력
#for i in range(1, n + 1):
#    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
#    if distance[i] == INF:
#        print("INFINITY")
#    # 도달할 수 있는 경우 거리를 출력
#    else:
#        print(distance[i])








#import sys

#sys.stdin = open("input.txt")

#def go(parent, graph, visited):
#    global res
#    visited[parent] = True

#    for child in graph[parent]:
#        if not visited[child]:
#            res[child] = parent
#            go(child, graph,visited)


#n = int(sys.stdin.readline().rstrip())

#graph = [[] for _ in range(n+1)]
#visited = [False]*(n+1)
#res = [None]*(n+1)


#for _ in range(n-1):
#    a, b = map(int, sys.stdin.readline().rstrip().split())
#    graph[a].append(b)
#    graph[b].append(a)

#go(1,graph,visited)

#for i in range(2,n+1):
#    print(res[i])







#import sys
#import math

#sys.stdin = open("input.txt")

#n, m = map(int,sys.stdin.readline().rstrip().split())

#print(n,m)

#chessboard = []
#min_result = math.inf
#temp = None
#cnt = 0
#res = [[0]*m for _ in range(n)]

#for i in range(n):
#    input = sys.stdin.readline().rstrip()
    
#    chessboard.append(list(input))
    
#    #chessboard[i] = input

##for c in chessboard:
##    print(c)

#for startRow in range(n-7):
#    for startCol in range(m-7):
#        temp = chessboard
#        cnt = 0

#        if temp[startRow][startCol] == 'B':

#            for i in range(startRow,startRow+7):
#                for j in range(startCol, startCol+7):
#                    pass

#            temp = chessboard
#            temp[startRow][startCol] = 'W'
#            res[startRow][startCol] = cnt
#            cnt = 0
#            for i in range(startRow,startRow+7):
#                for j in range(startCol, startCol+7):
#                    pass

#            if res[startRow][startCol] > cnt:
#                res[startRow][startCol] = cnt

#for startRow in range(n-7):
#    for startCol in range(m-7):
#        print(res[startRow][startCol], end= " ")
#    print()
