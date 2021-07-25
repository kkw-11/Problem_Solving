import sys

sys.stdin = open("input.txt","rt")

n = int(sys.stdin.readline().rstrip())

A = list(map(int,sys.stdin.readline().rstrip().split()))
res = [0]*n

for i in range(n-1):
    for j in range(i+1,n):
        if i-1 >=0 and res[i-1] == -1:
            if A[i-1] >= A[j]:
                print(-1, end=" ")
                res[i] = -1
                break
        if A[i] < A[j]:
            print(A[j],end= " ")
            break
    else:
        print(-1,end=" ")
        res[i] = -1
else:
    print(-1)