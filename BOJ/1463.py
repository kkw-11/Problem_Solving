import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
min_dis = [float("inf") for _ in range(n+1)]
min_dis[1] = 0
if n == 2:
    min_dis[2] = 1
elif n >= 3 and n <4:
    min_dis[2] = 1
    min_dis[3] = 1
elif n >= 4:
    min_dis[2] = 1
    min_dis[3] = 1
    min_dis[4] = 2

for num in range(5,n+1):
    if num % 6 == 0:
        min_val = min(min_dis[num//2],min_dis[num//3],min_dis[num-1])
        min_dis[num] = min_val + 1
    elif num % 3 == 0:
        min_val = min(min_dis[num//3],min_dis[num-1])
        min_dis[num] = min_val + 1
    elif num % 2 == 0:
        min_val = min(min_dis[num//2],min_dis[num-1])
        min_dis[num] = min_val + 1
    else:
        min_dis[num] = min_dis[num-1] + 1

print(min_dis[n])