#https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

# import sys 
#sys.stdin = open("input.txt","rt")
#인접리스트 방식으로 순위 표현
'''
idea는 각 플레리어의 경기 기록이 이미(n-1)이거나 현재 기록된 승패여부로 문제의 주어진 조건에 맞게 탐색을 통해 
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