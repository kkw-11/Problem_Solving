import sys
input = sys.stdin.readline

n = int(input())

if n <5:
    if n%3 == 0:
        print(n//3)
    else:
        print(-1)
else:
    max_five = n //5

    for i in range(max_five, -1, -1):
        mod_five = n - 5*i

        if mod_five % 3 == 0:
            print(i+mod_five//3)
            break
    else:
        print(-1)