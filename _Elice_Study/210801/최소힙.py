import sys
from heapq import heapify, heappop, heappush

#sys.stdin = open("input.txt","rt")

n = int(sys.stdin.readline().rstrip())

heap = []

for i in range(n):
    cmd = int(sys.stdin.readline().rstrip())

    if cmd > 0:
        heappush(heap, cmd)
    elif cmd == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))