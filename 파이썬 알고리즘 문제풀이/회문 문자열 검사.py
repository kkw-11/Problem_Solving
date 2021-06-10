import sys
#sys.stdin = open("input.txt","rt")

n = int(input())


for i in range(n):
    str1 = input()
    str1 = str1.lower()
    for j in range(len(str1)):
        if str1[j] != str1[-1-j]:
            # print("#",end="")
            # print(i+1,"NO")
            print("#%d NO" %(i+1))
            break
    else:
        # print("#",end="")
        # print(i+1,"YES")
        print("#%d YES" %(i+1))
