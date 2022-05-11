n = int(input())
space = n-1
star = 1
while space >= 0:
    for i in range(space):
        print(" ",end="")
    space -= 1
    for i in range(star):
        print("*",end="")
    print()
    star += 2