import sys
input = sys.stdin.readline
day = int(input())
numbers = list(map(int,input().split()))
cnt = 0
for number in numbers:
    if number == day:
        cnt += 1
print(cnt)