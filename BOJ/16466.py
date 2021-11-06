import sys

sys.stdin = open("input.txt")

n = int(sys.stdin.readline().rstrip())

tickets = list(map(int,sys.stdin.readline().rstrip().split()))

tickets.sort()

for i in range(n):
    if i+1 != tickets[i]:
        print(i+1)
        break
else:
    print(n+1)
