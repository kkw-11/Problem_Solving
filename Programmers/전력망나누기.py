from collections import deque

def solution(n, wires):
    answer = 101
    graph = [[] for _ in range(n+1)]
    #make graph
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    for wire in wires:
        checked = [False]*(n+1) 
        cnt = 1
        
        #BFS
        q = deque()
        q.append(wire[0])
        checked[wire[0]] = True
        checked[wire[1]] = True
        
        while q:
            cur_node = q.popleft()
            
            for next_node in graph[cur_node]:
                if not checked[next_node]:
                    checked[next_node] = True
                    q.append(next_node)
                    cnt += 1
                    
        dif = abs((n - cnt) - cnt)
        
        if dif < answer:
            answer = dif
    
    return answer
