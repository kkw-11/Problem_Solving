import sys
import heapq

MAX = 9999999999

n, m, k = map(int,sys.stdin.readline().rstrip().split())
bearinfo1 = []
bearinfo2 = []
bearinfo3 = []
tempBear = []
minValueC = MAX
totalV = 0

for i in range(k):
    v, c = list(map(int, sys.stdin.readline().rstrip().split()))
    heapq.heappush(bearinfo1,[-v,c])
    heapq.heappush(bearinfo2,[-v,c])
    heapq.heappush(bearinfo3,c)

minValueC = heapq.heappop(bearinfo3)

for i in range(n):
    totalV += -(heapq.heappop(bearinfo1)[0])


if totalV < m:
    print(-1)
else:
    while True:
        totalV = 0
        for i in range(n):
            while bearinfo2:
                bear = heapq.heappop(bearinfo2)
                tempBear.append(bear)

                if bear[1] <= minValueC:
                    totalV += -bear[0]
                    break
            
            if not bearinfo2:
                break
        
        if totalV < m:
            while True:
                curMinValueC = heapq.heappop(bearinfo3) # 간수치 주어진 맥주에서 그 다음으로 낮은 도수로 변경
                if curMinValueC > minValueC:
                    minValueC = curMinValueC
                    break
            for j in range(len(tempBear)):
                heapq.heappush(bearinfo2, tempBear.pop())
        else:
            print(minValueC)
            break
