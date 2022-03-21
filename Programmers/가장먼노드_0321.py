from collections import deque

def solution(n, vertex):
    answer = 0
    edges_cnt = [0]*(n+1)
    checked = [False]*(n+1)

    #make graph
    graph = [[] for _ in range(n+1)]

    for node in vertex:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])

    #BFS
    q = deque()
    q.append(1)
    checked[1] = True
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not checked[next]:
                checked[next] = True
                q.append(next)
                edges_cnt[next] = edges_cnt[cur] + 1

    max_cnt = max(edges_cnt)
    return edges_cnt.count(max_cnt)