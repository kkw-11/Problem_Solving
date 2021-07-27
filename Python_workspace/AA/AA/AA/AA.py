import sys
import heapq
sys.stdin = open("input.txt","rt")

n, m = map(int,sys.stdin.readline().rstrip().split())

cakes = list(map(int, sys.stdin.readline().rstrip().split()))

print(n,m)
print(cakes)

tenMulti = []
notTenMulti = []
answer = 0
curCutCnt = 0
totalCutCnt = 0

for cake in cakes:
    if cake == 10:
        answer += 1
    elif cake % 10 == 0 :
        heapq.heappush(tenMulti,cake)
    else:
        heapq.heappush(notTenMulti,cake)

print(tenMulti)
print(notTenMulti)

while tenMulti:
    cake = heapq.heappop(tenMulti)

    curCutCnt = cake // 10

    if curCutCnt > m - totalCutCnt:
        anser += m - totalCutCnt
        break
    elif curCutCnt == m - totalCutCnt:
        answer += (curCutCnt + 1)
        break
    else:
        answer += (curCutCnt + 1)
        totalCutCnt += curCutCnt
