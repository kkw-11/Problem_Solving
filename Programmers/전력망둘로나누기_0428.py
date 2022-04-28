def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n + 1)]

    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * (n + 1)
    child = [0] * (n + 1)

   # 노드 마다 자식 개수 구하기
    def child_count(node):
        nonlocal visited, answer
        visited[node] = True
        child_cnt = 1 # 자기자신 포함
        
        for next in tree[node]:
            if not visited[next]:
                visited[next] = True
                child_cnt += child_count(next)
        answer = min(answer,abs(n-child_cnt-child_cnt))
        return child_cnt #(현재 노드의 자식개수 + 자기자신) 부모에게 돌려주기

    child_count(1)

    return answer