import sys

input = sys.stdin.readline

milks = [0,1,2]
cnt = 0

n = int(input())
milk_markets = list(map(int,input().split()))

milk_sequence = 0

for index in range(n):
    if milk_markets[index] == milks[milk_sequence%3]:
        cnt += 1
        milk_sequence += 1
print(cnt)