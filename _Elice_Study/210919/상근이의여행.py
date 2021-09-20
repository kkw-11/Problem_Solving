import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    country, flight = map(int, sys.stdin.readline().rstrip().split())

    for j in range(flight):
        a, b = map(int, sys.stdin.readline().rstrip().split())
    
    print(country -1)


#dfs 풀이
# import sys

# input = sys.stdin.readline

# def go(cur,answer):
#     for next in graph[cur]:
#         if not visited[next]:
#             visited[next] = True
#             answer = go(next,answer+1)
#     return answer

# n = int(input())

# for _ in range(n):
#     answer = 0
#     country, flight = map(int, input().split())

#     graph = [[] for _ in range(country+1)]
#     visited = [False]*(country+1)
#     # graph 생성
#     for _ in range(flight):
#         country1, country2 = map(int, input().split())
#         graph[country1].append(country2)
#         graph[country2].append(country1)
#     else:
#         visited[1] = True
#         answer = go(1, 0)
#         print(answer)
