from collections import deque

def Count(v):
    global graph
    global numofChild
    if numofChild[v] != -1:
        return numofChild[v]

    count = len(graph[v])
    for child in graph[v]:
        count += Count(child)

    numofChild[v] = count
    return count

def MakeTree(n):
    global graph

    q = deque()
    q.append(1)
    while q:
        now = q.popleft()
        for new in graph[now]:
            q.append(new)
            graph[new].remove(now)
    return

graph = []
numofChild = []

def solution(n, wires):
    global graph
    global numofChild

    graph = [[] for _ in range(n + 1)]
    numofChild = [-1 for _ in range(n + 1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    MakeTree(n)
    Count(1)

    return min(map(lambda x: abs((n-(x + 1))-(x + 1)), numofChild))