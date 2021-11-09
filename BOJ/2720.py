import sys

input = sys.stdin.readline

quater = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01

coins = [quater,dime,nickel,penny]
coins = [coin * 100 for coin in coins]
test_case = int(input())
for _ in range(test_case):
    change = int(input())
    answer = []

    for coin in coins:
        answer.append(int(change//coin))
        change %= coin
    print(*answer)
