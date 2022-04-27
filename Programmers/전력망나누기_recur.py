def solution(n, wires):
    answer = float('inf')
    
    def DFS(cur_node, n, tree):
        nonlocal answer
        
        visited_cnt = 1
        for next_node in range(1,n+1):
            if tree[cur_node][next_node]:
                tree[cur_node][next_node] = False
                tree[next_node][cur_node] = False
                visited_cnt += DFS(next_node,n,tree)

                
        answer = min(answer,abs(n-visited_cnt-visited_cnt))        
        return visited_cnt
    
    
    tree = [[False]*(n+1) for _ in range(n+1)]
    for wire in wires:
        tree[wire[0]][wire[1]] = True
        tree[wire[1]][wire[0]] = True
        
    DFS(1,n,tree)    
    
    return answer