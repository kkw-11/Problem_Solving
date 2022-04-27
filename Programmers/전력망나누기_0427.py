def DFS(start, tree):
    stack = [start]
    checked = {start}
    
    while stack:
        cur_node = stack.pop()
        
        for next_node in tree[cur_node]:
            if next_node not in checked:
                stack.append(next_node)
                checked.add(next_node)
                
    return len(checked)
    

def solution(n, wires):
    answer = n
    tree = [set() for _ in range(n+1)]
    for wire in wires:
        tree[wire[0]].add(wire[1])
        tree[wire[1]].add(wire[0])
        
    for wire in wires:
        tree[wire[0]].remove(wire[1])
        tree[wire[1]].remove(wire[0])
        
        visited_cnt = DFS(wire[0],tree)
        result = abs(n - visited_cnt - visited_cnt)
        
        if result < answer:
            answer = result
        
        tree[wire[0]].add(wire[1])
        tree[wire[1]].add(wire[0])
        
    
    return answer