n = int(input())
coins = [5,2]
max_five = n // coins[0]
cnt = 0
while n>0:
    if (n % 5) % 2 == 0:
        print(n//5 + (n%5//2)+cnt)
        break
    else:
        n -= 2
        cnt += 1
print(-1)