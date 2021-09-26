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

        for node, dist_weight in graph[now]:
            cost = distance[now] + dist_weight

            if distance[node] > cost:
                distance[node] = cost
                heapq.heappush(q,(cost, node))

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