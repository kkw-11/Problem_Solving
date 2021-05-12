import sys
#sys.stdin = open("input.txt","rt")

T = int(input())
num = []
for i in range(T):
    N, s, e, k = map(int,input().split())
    num = list(map(int,input().split()))
    slicing = num[s-1:e]
    slicing.sort()
    print("#",i+1," ",end="")
    print(slicing[k-1])



