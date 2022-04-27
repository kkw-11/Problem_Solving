def solution(n, wires):
    
    def DFS(cur_node, tree, checked):
        nonlocal visited_cnt
        visited_cnt += 1
        checked[cur_node] = True
        
        for node in tree[cur_node]:
            if not checked[node]:
                checked[node] = True
                DFS(node,tree,checked)
                
    answer = n
    tree = [set() for _ in range(n+1)]
    for wire in wires:
        tree[wire[0]].add(wire[1])
        tree[wire[1]].add(wire[0])
        
    for wire in wires:
        tree[wire[0]].remove(wire[1])
        tree[wire[1]].remove(wire[0])
        
        visited_cnt = 0
        checked = [False]*(n+1)
        DFS(wire[0],tree,checked)
        result = abs(n - visited_cnt - visited_cnt)
        
        if result < answer:
            answer = result
        
        tree[wire[0]].add(wire[1])
        tree[wire[1]].add(wire[0])
    
    return answer