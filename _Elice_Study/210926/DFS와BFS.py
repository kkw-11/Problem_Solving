
# 인접리스트 방식
import sys
from collections import deque

def DFS(cur_node):
    global visited
    print(cur_node, end= " ")
    visited[cur_node] = True
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            DFS(next_node)
            
def BFS(start_node):
    global visited
    q= deque()

    q.append(start_node)
    visited[start_node] = True

    while q:
        pre_node = q.popleft()
        print(pre_node, end= " ")

        for next_node in graph[pre_node]:
            if not visited[next_node]:
                visited[next_node] = True

                q.append(next_node)

input = sys.stdin.readline

n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
for node_info in graph:
    node_info.sort()

DFS(start)
visited = [False]*(n+1)
print()
BFS(start)


##인접행렬 방식
# import sys
# from collections import deque

# def DFS(cur_node):
#     global visited
#     print(cur_node, end= " ")
#     visited[cur_node] = True
#     for next_node in range(1,n+1):
#         if graph[cur_node][next_node] == 1 and not visited[next_node]:
#             DFS(next_node)
   
# def BFS(start_node):
#     global visited
#     q= deque()

#     q.append(start_node)
#     visited[start_node] = True

#     while q:
#         pre_node = q.popleft()
#         print(pre_node, end= " ")
#         for next_node in range(1,n+1):
#             if graph[pre_node][next_node] == 1 and not visited[next_node]:
#                 visited[next_node] = True
#                 q.append(next_node)

# input = sys.stdin.readline

# n,m,start = map(int,input().split())
# graph = [[0]*(n+1) for _ in range(n+1)]
# visited = [False]*(n+1)

# for _ in range(m):
#     node1, node2 = map(int,input().split())
#     graph[node1][node2] = 1
#     graph[node2][node1] = 1


# DFS(start)
# visited = [False]*(n+1)
# print()
# BFS(start)