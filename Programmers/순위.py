from collections import deque

def solution(n, results):

    def DFS(start_node, cur, game_result, cnt):
        if cnt == n-1:
            return
        else:
            for next,res in graph[cur]:
               if not checked[next] and game_result == res:
                   game_cnt[start_node] += 1
                   checked[next] = True
                   DFS(start_node,next,game_result,cnt+1)
            return

    answer = 0
    game_cnt = [0]*(n+1)
    checked = [False]*(n+1)
    graph = [[] for _ in range(n+1)]

    #make graph
    for result in results:
        graph[result[0]].append((result[1],'W'))
        graph[result[1]].append((result[0],'L'))
    print(graph)

    for start_node in range(1,n+1):
        checked = [False]*(n+1)
        checked[start_node] = True
        DFS(start_node,start_node,'W',0)

        checked = [False]*(n+1)
        checked[start_node] = True
        DFS(start_node,start_node,'L',0)

    return game_cnt.count(n-1)