import sys

input = sys.stdin.readline
number, count = map(int,input().split())
numbers = list(map(int,input().split()))
range_sum = [0]*(number+1)
total = 0

for i in range(number):
    total += numbers[i]
    range_sum[i+1] = total

for _ in range(count):
    i, j = map(int,input().split())
    print(range_sum[j]-range_sum[i-1])
