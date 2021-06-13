
#스택 구현 DFS
from collections import defaultdict

def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    # 해쉬 딕셔너리로 특정 티켓의 인접 리스트로 그래프 표현
    # 2차원 배열, 인접리스트로 그래프를 표현하지 않고 해쉬 딕셔너리로 표현한 이유는 키값을 문자열로 지정 가능하기 때문
    # 2차원 배열과 인접리스트는 키값처럼 지정할 수 있는 값이 인덱스번호로 숫자만 가능하기 때문이다.
    def init_graph():
        routes = defaultdict(list) #key이 없을 경우 value 값을 빈 list로 default값 설정
        for key, value in tickets: 
            routes[key].append(value)
        return routes

    # 스택을 사용한 DFS
    def dfs():
        stack = ["ICN"]
        path = []  # 가려고하는 경로를 저장하는 변수
        while len(stack) > 0:  # stack이 비어있을 때까지
            top = stack[-1]
            # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    answer = dfs()
    return answer

# from collections import defaultdict

# def solution(tickets):
#     # 특정 티켓의 인접 리스트를 구하는 함수
#     def init_graph():
#         routes = dict()
#         for ticket in tickets:
#             if ticket[0] not in routes:
#                 routes[ticket[0]] = [ticket[1]]
#             else:
#                 routes[ticket[0]].append(ticket[1])
                
#         return routes

#     # 스택을 사용한 DFS
#     def dfs():
#         stack = ["ICN"]
#         path = []  # 가려고하는 경로를 저장하는 변수
#         while len(stack):  # stack이 비어있을 때까지
#             top = stack[-1]
#             # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
#             if top not in routes or len(routes[top]) == 0:
#                 path.append(stack.pop())
#             else:
#                 stack.append(routes[top].pop(0))
#         return path[::-1]

#     routes = init_graph()
#     for r in routes:
#         routes[r].sort()

#     answer = dfs()
#     return answer





##재귀를 이용한 DFS
# from collections import defaultdict 

# def dfs(graph, N, key, footprint):
#     if len(footprint) == N + 1:
#         return footprint

#     for idx, country in enumerate(graph[key]):
#         graph[key].pop(idx)

#         tmp = footprint[:]
#         tmp.append(country)

#         ret = dfs(graph, N, country, tmp)

#         graph[key].insert(idx, country)

#         if ret:
#             return ret


# def solution(tickets):
#     answer = []

#     graph = defaultdict(list)

#     N = len(tickets)
#     for ticket in tickets:
#         graph[ticket[0]].append(ticket[1])
#         graph[ticket[0]].sort()

#     answer = dfs(graph, N, "ICN", ["ICN"])

#     return answer
