import sys
import heapq

sys.stdin = open("input.txt")

day, sum_priority, kind = map(int,sys.stdin.readline().rstrip().split())
bear_info = []
total_priority = 0
bear_info_heap = []
find = False
for _ in range(kind):
    priority, alcohol = map(int, sys.stdin.readline().rstrip().split())
    bear_info.append((alcohol,priority))

bear_info.sort()

for bear in bear_info:
    total_priority += bear[1]
    heapq.heappush(bear_info_heap, bear[1])

    if len(bear_info_heap) == day:
        if total_priority >= sum_priority:
            find = True
            print(bear[0])
            break
        else:
            total_priority -= heapq.heappop(bear_info_heap)

if not find:
    print(-1)


