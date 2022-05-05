import sys
from collections import deque
def BFS(cur_node):
    global visited, tree
    visited[cur_node] = True
    q = deque()
    q.append(cur_node)
    cnt = 1

    while q:
        now = q.popleft()
        for next in tree[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                cnt += 1

    return cnt

input = sys.stdin.readline

n, m = map(int,input().split())

tree = [[] for _ in range(n+1)]
child_cnt = [0]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    tree[b].append(a)

max_cnt = -1

for start_node in range(1,n+1):
    visited = [False]*(n+1)
    child_cnt[start_node] = BFS(start_node)
    if max_cnt < child_cnt[start_node]:
        max_cnt = child_cnt[start_node]

for node_num, cnt in enumerate(child_cnt):
    if cnt == max_cnt:
        print(f"{node_num} ", end="")