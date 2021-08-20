import sys
n = int(sys.stdin.readline().rstrip())

slimes = list(map(int, sys.stdin.readline().rstrip().split()))

res = 0

while len(slimes) != 1:
    slime1 = slimes.pop()
    slime2 = slimes.pop()
    res += (slime1*slime2)

    slimes.append(slime1+slime2)

print(res)
