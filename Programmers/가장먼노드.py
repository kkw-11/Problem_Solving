from collections import deque

def solution(n, vertex):
    answer = 0
    edges_cnt = [0]*(n+1)
    start = 1
    #make graph
    checked = [False]*(n+1)
    graph = [None]*(n+1)
    for node in range(n+1):
        graph[node] = []

    for edge in vertex:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    #graph search - BFS
    q = deque()
    q.append(start)
    checked[start] = True

    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            if not checked[next]:
                q.append(next)
                checked[next] = True
                edges_cnt[next] = edges_cnt[cur] + 1

    max_cnt = max(edges_cnt)
    return edges_cnt.count(max_cnt)