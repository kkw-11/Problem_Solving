import sys
input = sys.stdin.readline
numbers = list(map(int,input().split()))
total = 0
for number in numbers:
    total += number**2
print(total%10)