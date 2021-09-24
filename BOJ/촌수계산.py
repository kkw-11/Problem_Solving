import sys

input = sys.stdin.readline

people = int(input())

a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(people+1)]
visited = [False]*(people+1)
answer = -1
flag = False

for _ in range(m):
    parent, child = map(int,input().split()) 
    graph[parent].append(child)
    graph[child].append(parent)

def find(person,relation):
    global answer, flag
    visited[person] = True
    if person == b:
        print(relation)
        flag = True
        return
    for p in graph[person]:
        if not visited[p]:
            find(p, relation+1)
find(a,0)
if not flag:
    print(-1)