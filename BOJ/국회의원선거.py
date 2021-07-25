# https://www.acmicpc.net/problem/1417

import sys
from heapq import heapify, heappush, heappop

#sys.stdin = open("input.txt","rt")

n = int(sys.stdin.readline().rstrip())
heap = []

for i in range(n):
    score = int(sys.stdin.readline().rstrip())
    if i == 0:
        dasom = score
    else:
        heappush(heap,[-score,score,i+1])


cnt = 0

if n == 1:
    print(0)
else:
    while True:
        maxInfo = heappop(heap)

        if maxInfo[1] < dasom:
            break
        else:
            cnt += 1
            maxInfo[0] += 1
            maxInfo[1] -= 1
            dasom += 1
            heappush(heap,maxInfo)

    print(cnt)
