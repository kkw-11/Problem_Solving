
from collections import defaultdict
cnt = 0
ticketSize = 0
destination = ""
answer  = []
res  = []

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["ICN","AAA"],["AAA","BBB"],["IAD","ICN"]]

'''
ICN:[(AAA,0),(JFK,0)] 
JFK:[(HND,0)]
HND:[(IAD,0)]
IAD:[(ICN,0)]
AAA:[(BBB)]
'''
## 스택을 사용한 DFS
def dfs(routes, start, moveCnt):
    global res
    global answer
    global ticketSize
    if moveCnt == ticketSize - 1:
        for elemToVal in routes[start]:
            if elemToVal[1] == 0:
                elemToVal[1] = 1
                answer.append(elemToVal[0])
                res = answer[:]
                return answer
    else:
        for elemToVal in routes[start]:
            if elemToVal[1] == 0:
                elemToVal[1] = 1 #방문 체크
                answer.append(elemToVal[0])
                dfs(routes,elemToVal[0],moveCnt+1)
                elemToVal[1] = 0 #방문체크 해제
                answer.pop()


def solution(tickets):
    global ticketSize 
    global res
    ticketSize = len(tickets) # 6
    # 해쉬 딕셔너리로 tickets 정보 인접 리스트 그래프로 표현
    routes = defaultdict(list)
    for fromKey, toValue in tickets: 
        routes[fromKey].append([toValue,0])
        
    for rKey in routes:
        routes[rKey].sort()


    print(routes)   
    print(destination)
    answer.append("ICN")
    dfs(routes,"ICN",0)
    
    return res

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["ICN","AAA"],["AAA","BBB"],["IAD","ICN"]]
print(solution(tickets))

