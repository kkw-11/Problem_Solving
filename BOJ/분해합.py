import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    res = 0
    temp = i
    while temp:
        num = temp%10
        temp //= 10
        res += num

    if res+i == n:
        print(i)
        break
else:
    print(0)

