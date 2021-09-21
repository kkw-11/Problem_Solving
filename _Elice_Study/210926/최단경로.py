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
distance = [999999999]*(number_of_node+1)

start = int(input())

for _ in range(number_of_edge):
    from_node, to_node, weight = map(int,input().split())
    #for node_info in graph[from_node]:
    #    if node_info[0] == to_node:
    #        if node_info[1] > weight:
    #            node_info[1] = weight
    #            break
    #else:
    graph[from_node].append([to_node,weight])

dijkstra(start)
for d in distance[1:]:
    if d == 999999999:
        print("INF")
    else:
        print(d)

# ## 다른 사람 풀이
# import sys, heapq, collections

# sys.stdin = open("input.txt")

# def dijkstra(start):
    
#     q = []
#     heapq.heappush(q,(0,1))

#     while q:
#         path, p = heapq.heappop(q)
#         if path < distance[p]:
#             distance[p] = path
#             for nxt_p, dist in graph[p]:
#                 if distance[nxt_p] == float('INF'):
#                     heapq.heappush(q,(path + dist, nxt_p))
            

# input = sys.stdin.readline
# number_of_node, number_of_edge = map(int,input().split())
# graph = [[] for _ in range(number_of_node+1)]
# for _ in range(number_of_edge):
#     a, b, c = map(int,input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))
    
# distance = [float('INF')] * (number_of_node+1)

# dijkstra(1)
# print(distance[number_of_node])