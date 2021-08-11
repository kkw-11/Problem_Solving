import sys

n = int(sys.stdin.readline().rstrip())

temp = 666
cnt = 1

while True:

    if "666" in str(temp):
        cnt += 1

    if cnt == n:
        print(temp)
        break

    temp = temp + 1
