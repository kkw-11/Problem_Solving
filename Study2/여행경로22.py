from collections import defaultdict
answer  = []
last = ""
# 스택을 사용한 DFS
def dfs(routes, start):

    global answer
    answer.append(start)
    # ["ICN":["SFO","ATL"]]
    for idx, toValue in enumerate(routes[start]):
        if routes[start][idx] in routes:  #도착점이 routes에 key로 있어야 그 곳에서 다시 출발할 수 있음
            routes[start].pop(idx)
            dfs(routes,toValue)

def solution(tickets):
    # 해쉬 딕셔너리로 특정 티켓의 인접 리스트로 그래프 표현
    routes = defaultdict(list)
    for fromKey, toValue in tickets: 
        routes[fromKey].append(toValue)
        
    for rKey in routes:
        routes[rKey].sort()

    dfs(routes,"ICN")
    # answer.extend(routes[answer[-1]])
    answer.append(routes[answer[-1]])
    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["ICN","AAA"],["AAA","BBB"]]

print(solution(tickets))