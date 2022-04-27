def solution(n, wires):
    tree = [[] for _ in range(n + 1)]

    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * (n + 1)
    child = [0] * (n + 1)

   # 노드 마다 자식 개수 구하기
    def DFS(node):
        nonlocal child, visited
        visited[node] = True
        
        for next in tree[node]:
            if not visited[next]:
                visited[next] = True
                child[node] += DFS(next)

        return child[node] + 1 #(현재 노드의 자식개수 + 자기자신) 부모에게 돌려주기

    DFS(1)
    result = n
    print(child)
    for c in child:
        result = min(result, abs(n - 2 * (c + 1)))
    return min(map(lambda x: abs(n -(x+1)*2),child ))
    return result