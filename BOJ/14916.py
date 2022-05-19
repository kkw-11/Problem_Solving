n = int(input())
coins = [5,2]
max_five = n // coins[0]

while True:
    if (n -(coins[0]*max_five)) % 2 == 0:
        print(max_five + (n -(coins[0]*max_five)) // 2)
        break
    else:
        max_five -= 1
        if max_five == -1:
            print(-1)
            break