

from collections import defaultdict

def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes
'''
init_graph 예외처리로 생성1
    # # 특정 티켓의 인접 리스트를 구하는 함수, 키값 존재 여부 확인 예외처리
    # def init_graph():
    #     routes = dict()
    #     for ticket in tickets:
    #         if ticket[0] in routes:
    #             routes[ticket[0]].append(ticket[1])
    #         else: #route에 key값 ticket[0]이 존재하지 않는 다면 ticket[0] 키값과 ticket[1] 리스트 지정 
    #             routes[ticket[0]] = [ticket[1]]
    #     return routes
    
init_graph 예외처리로 생성2
    # # 특정 티켓의 인접 리스트를 구하는 함수
    # def init_graph():
    #     routes = dict()
    #     for ticket in tickets:
    #         if ticket[0] not in routes:
    #             routes[ticket[0]] = [ticket[1]]
    #         else:
    #             routes[ticket[0]].append(ticket[1])
                
    #     return routes
'''

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


# def solution(tickets):
#     routes = {} # 딕셔너리 선언
#     for ticket in tickets:
#         routes[ticket[0]] = routes.get(ticket[0], []) + [ticket[1]]
#     print(routes)
#     for route in routes:
#         routes[route].sort(reverse=True)
#     stack = ['ICN']
#     path = []
#     while stack:
#         top = stack[-1]
#         if top in routes and routes[top]:
#             stack.append(routes[top].pop())
#         else:
#             path.append(stack.pop())
#     return path[::-1]

