import sys
from collections import deque

sys.stdin = open("input.txt")

N, K = map(int,sys.stdin.readline().rstrip().split())

check = [False]*(N+1)
check[0] = True

q = deque()
res = []
cnt = 0
for i in range(1,N+1):
    q.append(i)

while q:
    for i in range(K):
        num = q.popleft()
        if i == K-1:
            res.append(num)
        else:
            q.append(num)

print("<",end="")
for i in range(N-1):
    print(res[i],end="")
    print(", ",end="")
else:
    print(res[N-1],end="")
    print(">",end="")
