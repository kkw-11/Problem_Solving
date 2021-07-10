# https://www.acmicpc.net/problem/5014
from collections import deque


def bfs(F, S, G, U, D):
    q = deque([[S, 0]])
    visited = {S}

    while q:
        floor, cnt = q.popleft()
        if floor == G:  # 목표 층에 도착
            return cnt
        if floor + U <= F and floor + U not in visited:  # 위층으로 이동
            q.append([floor + U, cnt + 1])
            visited.add(floor + U)
        if floor - D >= 1 and floor - D not in visited:  # 아래층으로 이동
            q.append([floor - D, cnt + 1])
            visited.add(floor - D)

    return "use the stairs"


if __name__ == "__main__":

    F, S, G, U, D = map(int, input().split())

    print(bfs(F, S, G, U, D))