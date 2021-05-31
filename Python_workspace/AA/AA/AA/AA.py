#import sys
##sys.stdin = open("input.txt","rt")

#n = int(input())
#cnt = 0
#ch = [0]*(n+1)


#for i in range(2,n+1):
#    if ch[i] == 0:
#        cnt += 1
#        for j in range(i,n+1,+i):
#            ch[j] = 1

#print(cnt)
        





import sys
#sys.stdin = open("input.txt","rt")

cnt = 0
def isPrime(x):
    if(x == 2 ):
        return 1
    temp =int(x/2)
    for i in range(2,temp+1):
        if x % i == 0:
            return 1
    return 0

n = int(input())
for i in range(2,n+1):
    flag = isPrime(i)
    if flag != 1:
        cnt += 1

print(cnt+1)
