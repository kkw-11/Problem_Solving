import sys 
from collections import deque

def BFS(start = 1):
    
    q = deque()
    
    visited[start] = True
    q.append((start,0))


    while q:
       now, move_count = q.popleft()
       answer[now] = move_count
       
       for next in graph[now]:
           if not visited[next]:
               visited[next] = True
               q.append((next, move_count+1))


input = sys.stdin.readline

number_of_city , number_of_street = map(int,input().split())

graph = [[] for _ in range(number_of_city+1)]
visited = [False]*(number_of_city+1)

for _ in range(number_of_street):
    city1, city2 = map(int,input().split())
    graph[city1].append(city2)
    graph[city2].append(city1)

number_of_maintenance = int(input())

for _ in range(number_of_maintenance):
    city1, city2 = map(int,input().split())
    graph[city1].append(city2)
    graph[city2].append(city1)
    
    answer = [-1]*(number_of_city+1)
    BFS()
    print(*answer[1:number_of_city+1])
    visited = [False]*(number_of_city+1)