import sys

input = sys.stdin.readline

milks = [0,1,2]
cnt = 0

number_of_markets = int(input())
market_milk = list(map(int,input().split()))

milk_sequence = 0

for market_number in range(number_of_markets):
    if market_milk[market_number] == milks[milk_sequence]:
        cnt += 1
        milk_sequence += 1
        milk_sequence %= 3
print(cnt)