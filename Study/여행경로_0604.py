# #https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3

def solution(tickets):
    routes = dict()
    for ticket in tickets:
        if ticket[0] in routes:
            routes[ticket[0]].append(ticket[1])
        else:
            routes[ticket[0]] = ticket[1]

    for route in routes.keys():
        routes[route].sort(reverse= True)

    stack = ["ICN"]
    answer = []
    while stack:
        top = stack[-1]
        # 현재 stack에 탑은 출발지
        # 찾고싶은 키값 in 딕셔너리
        if top not in routes or len(routes[top] == 0):
            answer.append(stack.pop())
        else:
            stack.append(routes[top])



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