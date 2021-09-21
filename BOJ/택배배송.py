import sys
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, cur_node = heapq.heappop(q)
        if distance[cur_node] < dist:
            continue
        
        distance[cur_node] = dist

        for next_node, weight in graph[cur_node]:
            cost = distance[cur_node] + weight

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost, next_node))

INF = float("inf")
input = sys.stdin.readline

number_of_node, number_of_edge = map(int,input().split())

graph = [[] for _ in range(number_of_node+1)]
distance = [INF]*(number_of_node+1)


for _ in range(number_of_edge):
    from_node, to_node, weight = map(int,input().split())
    
    graph[from_node].append((to_node,weight))
    graph[to_node].append((from_node,weight))

dijkstra(1)
print(distance[number_of_node])