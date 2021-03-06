def solution(n, wires):
    answer = float('inf')
    
    def DFS(cur_node, n):
        nonlocal answer, tree, visited
        visited[cur_node] = True
        
        child_cnt = 1
        for next_node in range(1,n+1):
            if tree[cur_node][next_node] and not visited[next_node]:
                visited[next_node] = True
                child_cnt += DFS(next_node,n)
                
        answer = min(answer,abs(n-child_cnt-child_cnt))        
        return child_cnt
    
    
    tree = [[False]*(n+1) for _ in range(n+1)]
    for wire in wires:
        tree[wire[0]][wire[1]] = True
        tree[wire[1]][wire[0]] = True
    visited = [False for _ in range(n+1)]
    DFS(1,n)    
    
    return answer