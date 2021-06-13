#https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

# import sys 
#sys.stdin = open("input.txt","rt")
#인접리스트 방식으로 순위 표현
'''
idea는 각 플레리어의 경기 기록 수가 이미 (n-1)개 이거나 현재 기록된 승패여부로 문제의 주어진 조건에 맞게 탐색을 통해 
승,패 알 수 있는 선수의 수가 (n-1)개수이면 순위를 만들 수 있음
 ex) 5가 2한테 지면 5는 2를 이기는 애들한테 모두 진다. 이 방식으로 현재 기록으로 나머지 선수들과의 승패여부 탐색 확인
 이렇게 확인 된 수가 n-1이 되면 됨
'''
cnt = 0

def DFS(n, graph, visited, vertex,flag):

    visited[vertex] = True
    global cnt
    #        [ 0    1         2                                   3                  4                5     ] 
    #graph = [[], [(2, 1)], [(4, -1), (3, -1), (1, -1), (5, 1)], [(4, -1), (2, 1)], [(3, 1), (2, 1)], [(2, -1)]]

    # 승 방향 그래프 탐색
    if flag == 1:
        for info in graph[vertex]: # vertex:2, graph node: (4, -1), (3, -1), (1, -1), (5, 1)
            if info[1] == 1 and visited[info[0]] != 1:
                cnt += 1
                DFS(n, graph,visited,info[0],flag)
    # 패 방향 그래프 탐색
    elif flag == -1:
        for info in graph[vertex]:
            if info[1] == -1 and visited[info[0]] != 1:
                cnt += 1
                DFS(n,graph,visited,info[0],flag)

    return 

def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    global cnt

    # 입력 값으로 인접리스트 그래프 만들기
    #results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    for result in results: # result: [4, 3], [4, 2], [3, 2], [1, 2], [2, 5]
        graph[result[0]].append((result[1], 1)) #result[0]이 result[1]한테 이긴다.
        graph[result[1]].append((result[0], -1)) #result[1]이 result[0]한테 진다. 

    # print(graph)
    # print()
    #        [ 0    1         2                                   3                  4                5     ] 
    #graph = [[], [(2, 1)], [(4, -1), (3, -1), (1, -1), (5, 1)], [(4, -1), (2, 1)], [(3, 1), (2, 1)], [(2, -1)]]
     # graph[1] (2,1)
    for player in range(1,n+1):
        if len(graph[player]) == n-1:
            answer +=1
            continue

        for j in range(1,n+1):
            visited[j]= False
        cnt = 0

        # 승 수 계산
        DFS(n, graph,visited,player,1)
        '''
        # 한 player가 다른 player에게 이기면서 지는 경우는 없기 때문 (player 2: (4,1) (4,-1) 동시에 있는 경우는 없기 때문) 현재 player Vertex에서 
        # 시작할 때 승수 체크전 한번만 초기화 하면 됨 방문한 곳을 다시 방문할 일이 없음
        '''
        # for j in range(1,n+1): 
        #     visited[j]= False  

        # 패 수 계산
        DFS(n,graph,visited,player,-1)

        if cnt == n-1:
            answer += 1

    return answer
graph = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
n = 5

print(solution(n,graph))

# #https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
# # import sys 
# #sys.stdin = open("input.txt","rt")
# #인접행렬 방식으로 그래프 표현
# cnt = 0
# def DFS(graph, visited, vertex,flag,n):
#     visited[vertex] = 1
#     global cnt
#     if flag == 1:
#         for i in range(1,n+1):
#             if graph[vertex][i] == 1 and visited[i] != 1:
#                 cnt += 1
#                 DFS(graph,visited,i,flag,n)
#     elif flag == -1:
#         for i in range(1,n+1):
#             if graph[vertex][i] == -1 and visited[i] != 1:
#                 cnt += 1
#                 DFS(graph,visited,i,flag,n)

#     return 

# def solution(n, results):
#     answer = 0
#     graph = [[0]*(n+1) for _ in range(n+1)]
#     ch = [0]*(n+1)
#     global cnt

#     # 입력 값으로 그래프 만들기
#     for result in results:
#         graph[result[0]][result[1]] = 1
#         graph[result[1]][result[0]] = -1

#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             ch[j]= 0
#         cnt = 0
#         # 승 수 계산
#         DFS(graph,ch,i,1,n)

#         for j in range(1,n+1):
#             ch[j]= 0
#         # 패 수 계산
#         DFS(graph,ch,i,-1,n)

#         # 승수와 패수를 모두 계산한
#         if cnt == n-1:
#             answer += 1

#     return answer

#여행경로의 플로이드 와샬 풀이
# '''플로이드 와샬 알고리즘 (Floyd Warshall Algorithm)
# # n = 노드 개수

# for k in range(n):			# 모든 노드를 중간점으로 삼으면서
# 	for i in range(n):		# 거리행렬을 순회
#     	for j in range(n):	
#             if arr[i][j] > arr[i][k] + arr[k][j]:	# 이때, 원래 저장돼 있던 i부터 j까지의 거리보다 
#                 arr[i][j] = arr[i][k] + arr[k][j]	# k를 거쳐가는 i-k-j 거리가 더 짧다면 갱신함

# 거리행렬? https://zetawiki.com/wiki/%EA%B1%B0%EB%A6%AC_%ED%96%89%EB%A0%AC
# '''

# from collections import Counter


# def solution(n, results):
#     # p1이 p2에 이겼을 때는 1로,
#     # p1이 p2에 졌을 때는 -1로 초기화. (거리가 아니라 승패 여부만 저장한다.)
#     board = [[0] * n for _ in range(n)]
#     for p1, p2 in results: #(0,0 배열부터)
#         board[p1 - 1][p2 - 1] = 1 #이긴놈은 1, 진놈은 -1
#         board[p2 - 1][p1 - 1] = -1

#     for k in range(n):                  # 1. 모든 노드를 중간점(경로)로 가정하며
#         for i in range(n):              # 2. 점수판을 순회
#             for j in range(n):          # 3. 만약 i가 k에 이겼고, k가 j에 이겼다면
#                 if board[i][j] == 0:    # i는 j에게도 이김 (지는 것도 동일)  //0이라는건 아직 승패를 모른다는 것. 초기화 상태 그대로
#                     if board[i][k] == 1 and board[k][j] == 1:
#                         board[i][j] = 1 #승패 결정
#                     elif board[i][k] == -1 and board[k][j] == -1:
#                         board[i][j] = -1 #승패 결정

#     # 각 노드 점수판에 0이 하나(다른 노드들에 대해 승패가 모두 결정됨)인 경우만 셈
#     ans = 0
#     for i in range(n):
#         if Counter(board[i])[0] == 1: #Counter : 컨테이너에 중복 몇 개 있는지. #https://appia.tistory.com/176
#             ans += 1 #0이 하나다? 그럼 승패 결정됨
#     return ans

# # https://summa-cum-laude.tistory.com/16