import sys
from collections import deque


def BFS(start):
    visited[start] = True
    q = deque()
    q.append((start,0))

    while q:
        now, cnt = q.popleft()

        if answer[start] < cnt:
            answer[start] = cnt

        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append((next,cnt+1))

input = sys.stdin.readline

number_of_members = int(input())
graph = [[] for _ in range(number_of_members+1)]
visited = [False]*(number_of_members+1)
answer = [0]*(number_of_members+1)

while True:
    member1, member2 = map(int,input().split())

    if member1 == -1 and member2 == -1:
        break
    
    graph[member1].append(member2)
    graph[member2].append(member1)

for start in range(1,number_of_members+1):
    BFS(start)
    visited = [False]*(number_of_members+1)

min_cnt = min(answer[1:])
number_of_candidate = answer.count(min_cnt)

print(min_cnt, number_of_candidate)

for i in range(1,number_of_members+1):
    if answer[i] == min_cnt:
        print(i, end=" ")
