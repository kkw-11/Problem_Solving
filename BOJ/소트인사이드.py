import sys

res= 0
n = list(map(int,sys.stdin.readline().rstrip()))

n.sort(reverse= True)

for i in range(len(n)):
    res = res * 10 + n[i]
print(res)
