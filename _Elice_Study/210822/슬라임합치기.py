import sys
import heapq
sys.stdin = open("input.txt")

n = int(sys.stdin.readline().rstrip())

slimes = list(map(int, sys.stdin.readline().rstrip().split()))

heapq.heapify(slimes)

res = 0

while len(slimes) != 1:
    slime1 = heapq.heappop(slimes)
    slime2 = heapq.heappop(slimes)
    res += (slime1*slime2)
    heapq.heappush(slimes, slime1+slime2)

print(res)
