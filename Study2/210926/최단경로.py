import sys
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        distance[now] = dist

        for node_info in graph[now]:
            cost = distance[now] + node_info[1]

            if cost < distance[node_info[0]]:
                distance[node_info[0]] = cost
                heapq.heappush(q,(cost, node_info[0]))

input = sys.stdin.readline

number_of_node, number_of_edge = map(int,input().split())

graph = [[] for _ in range(number_of_node+1)]
INF = float("inf")
distance = [INF]*(number_of_node+1)

start = int(input())
for _ in range(number_of_edge):
    from_node, to_node, weight = map(int,input().split())

    graph[from_node].append([to_node,weight])

dijkstra(start)
for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)


# ## indigo0316님  풀이
# import sys, heapq, collections
# input = sys.stdin.readline
# V, E = map(int,input().split())
# K = int(input())
# graph = collections.defaultdict(list)
# for _ in range(E):
#     a, b, c = map(int,input().split())
#     graph[a].append((b,c))
    
# answer = [float('INF')] * (V+1)
# q = []
# heapq.heappush(q,(0,K))

# while q:
#     path, p = heapq.heappop(q)
#     if path < answer[p]:
#         answer[p] = path
#         for nxt_p, dist in graph[p]:
#             if answer[nxt_p] == float('INF'):
#                 heapq.heappush(q,(path + dist, nxt_p))
            
# for i in range(1, len(answer)):
#     print(answer[i] if answer[i] != float('INF') else 'INF')

