#import sys
##sys.stdin = open("input.txt","rt")
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
#res = set() #중복제거하는 set 자료구조

#for i in range(n):
#    for j in range(i+1,n):
#        for m in range(j+1,n):
#            res.add(a[i]+a[j]+a[m])


#res = list(res)
#res.sort(reverse = True)
#print(res[k-1])


import sys
sys.stdin = open("input.txt","rt")
n,k = map(int,input().split())
card = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(card[i]+card[j]+card[m])


res = list(res)
res.sort(reverse = True)
print(res[k-1])