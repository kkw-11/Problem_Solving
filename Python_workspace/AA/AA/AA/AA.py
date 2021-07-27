import sys

input_data = sys.stdin.readline().rstrip()
cnt = [0] * 26
maxCnt = 0
idx = list()

for elem in input_data:
    ascii = ord(elem)

    if ascii >= 65 and ascii <= 90:
        cnt[ascii - 65] += 1
    elif ascii >= 97 and ascii <=122:
        cnt[ascii - 97] += 1

maxCnt = max(cnt)

for i in range(len(cnt)):
    if maxCnt == cnt[i]:
        idx.append(i)

if len(idx) == 1:
    print(chr(idx[0]+65))
elif len(idx) > 1:
    print("?")

#import sys
#import heapq
#sys.stdin = open("input.txt","rt")

#n, m = map(int,sys.stdin.readline().rstrip().split())

#cakes = list(map(int, sys.stdin.readline().rstrip().split()))

#print(n,m)
#print(cakes)

#tenMulti = []
#notTenMulti = []
#answer = 0
#curCutCnt = 0
#totalCutCnt = 0

#for cake in cakes:
#    if cake == 10:
#        answer += 1
#    elif cake % 10 == 0 :
#        heapq.heappush(tenMulti,cake)
#    else:
#        heapq.heappush(notTenMulti,cake)

#print(tenMulti)
#print(notTenMulti)

#while tenMulti:
#    cake = heapq.heappop(tenMulti)

#    curCutCnt = cake // 10

#    if curCutCnt > m - totalCutCnt:
#        anser += m - totalCutCnt
#        break
#    elif curCutCnt == m - totalCutCnt:
#        answer += (curCutCnt + 1)
#        break
#    else:
#        answer += (curCutCnt + 1)
#        totalCutCnt += curCutCnt
