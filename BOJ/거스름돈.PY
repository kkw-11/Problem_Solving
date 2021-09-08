import sys

n = int(input())

coins = [500,100,50,10,5,1]
answer = 0
changes = 1000 - n
for coin in coins:
    if changes // coin > 0:
        answer += n//coin
        changes %= coin
    if changes == 0:
        break

print(answer)