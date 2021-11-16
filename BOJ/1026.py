import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
total = 0
a.sort()
b.sort(reverse=True)

for i in range(n):
    total += a[i]*b[i]
print(total)