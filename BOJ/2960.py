import sys

n, k= map(int, sys.stdin.readline().rstrip().split())

deleteCheck = [False]*(n+1)

cnt = 0
for i in range(2,n+1):
    for j in range(i,n+1,i):
        if deleteCheck[j] == False:
           
            deleteCheck[j] = True
            cnt += 1
            if cnt == k:
                print(j)
                break
    if cnt == k:
        break
  