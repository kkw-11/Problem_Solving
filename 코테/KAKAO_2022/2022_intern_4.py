from collections import deque
answer = []
def DFS(graph,checked, cur, cost, start, end,  intensity, max_intensity):
    global answer
    if max_intensity < cost:
        max_intensity = cost
    if cur == end:
        if intensity[start][end] > max_intensity:
            intensity[start][end] = max_intensity
            answer.append((end,max_intensity))
            return
    else:
        
        for next_node, cost in graph[cur]:
            
            if not checked[next_node]:
                temp = max_intensity
                if cost > max_intensity:
                    max_intensity = cost
                checked[next_node] = True
                DFS(graph,checked,next_node,cost,start,end,intensity,max_intensity)
                max_intensity = temp
                checked[next_node] = False


def solution(n, paths, gates, summits):
    global answer
    intensity = [ [float("inf")]*(n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    checked = [False]*(n+1)

    for path in paths:
        graph[path[0]].append((path[1],path[2]))
        graph[path[1]].append((path[0],path[2]))
    max_intensity = 0
    summits.sort()
    for gate in gates:
        for summit in summits:
            DFS(graph, checked, gate, 0, gate, summit, intensity, max_intensity)  

    answer.sort(key = lambda x: x[1])
    print(answer)
    min_intensity = float("inf")
    result = [answer[0],answer[1]]


    return answer

n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3,7]
summits = [1,5]

print(solution(n, paths, gates, summits))


