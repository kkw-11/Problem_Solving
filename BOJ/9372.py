import sys

def DFS(cur, answer):
    visited[cur] = True

    for next in graph[cur]:
        if visited[next] == False:
            answer = DFS(next, answer+1)

    return answer

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    countryOfNum, flightOfNum = map(int, sys.stdin.readline().rstrip().split())

    #graph 생성
    graph = [[] for _ in range(countryOfNum+1)]
    visited = [False]*(countryOfNum+1)

    for j in range(flightOfNum):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    else:
        answer = 0
        answer = DFS(1, 0)
        print(answer)

## 두번째 풀이
# import sys

# n = int(sys.stdin.readline().rstrip())

# for i in range(n):
#     countryOfNum, flightOfNum = map(int, sys.stdin.readline().rstrip().split())

#     for j in range(flightOfNum):
#         a, b = map(int, sys.stdin.readline().rstrip().split())
    
#     print(countryOfNum -1)        