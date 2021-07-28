import sys
from heapq import heapify, heappush, heappop

#sys.stdin = open("input.txt","rt")

n = int(sys.stdin.readline().rstrip())

heap = []

for _ in range(n):
    cmd = int(sys.stdin.readline().rstrip())

    if cmd == 0:
        if len(heap):
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap, (abs(cmd),cmd))