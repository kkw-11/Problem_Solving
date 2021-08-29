import sys
import heapq

day, sum_priority, kind = map(int,sys.stdin.readline().rstrip().split())
beer_info = []
total_priority = 0
beer_info_heap = []
find = False

# 2,5  4,6  3,3  4,3  1,4
for _ in range(kind):
    priority, alcohol = map(int, sys.stdin.readline().rstrip().split())
    beer_info.append((alcohol, priority)) # 

beer_info.sort()

for beer in beer_info: # beer = 2,5 
    total_priority += beer[1] # beer[0] alcohol, beer[1] priority
    heapq.heappush(beer_info_heap, beer[1]) # 최소힙  

    if len(beer_info_heap) == day:
        if total_priority >= sum_priority:
            find = True
            print(beer[0])
            break
        else:
            total_priority -= heapq.heappop(beer_info_heap)

if not find:
    print(-1)

