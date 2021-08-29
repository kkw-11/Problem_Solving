import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    node1, node2, cost = map(int, input().split())
    
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    for j in range(len(graph[node1])):
        origin_node2, origin_cost = graph[node1][j][0], graph[node1][j][1]
        if node2 == origin_node2:
            if origin_cost > cost:
                graph[node1][j] = (node2, cost)
            break
    else:
        graph[node1].append((node2, cost))

# 시작 노드, 도착 노드 번호를 입력받기
start, end = map(int, input().split())

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for node_info in graph[start]:
        distance[node_info[0]] = node_info[1]
        
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for node_info in graph[now]:
            cost = distance[now] + node_info[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[node_info[0]]:
                distance[node_info[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)
print(distance[end])