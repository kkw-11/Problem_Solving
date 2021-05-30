import sys
#sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())

cnt = [0]*(n+m+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j] += 1

#maxCnt = max(sum)

maxCnt = 0
for i in range(len(cnt)):
    if maxCnt < cnt[i]:
        maxCnt = cnt[i]


for i in range(len(cnt)):
    if cnt[i] == maxCnt:
        print(i, end= " ")