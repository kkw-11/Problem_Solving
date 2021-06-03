import sys
sys.stdin = open("input.txt","rt")

def reverse(x):
    #reverseNum = ""
    reverseNum = 0
    while x>0:
        temp = x%10
        reverseNum = reverseNum*10 + temp
        x //= 10
    ##숫자를 뒤집는 방법
    #str1 = str(x) # 3 2 1
    #reverseNum = ''
    ##for char in str1:
    ##    reverseNum = char + reverseNum
    ##for i in range(0,len(str1)):
    ##    reverseNum = str1[i] + reverseNum
    #for i in range(len(str1)-1,-1,-1):
    #    reverseNum = reverseNum + str1[i]
    
    return reverseNum

def isPrime(x):
    for i in range(2,int(x/2)+1):
        if x % i == 0:
            return 0
    else:
        return 1


n = int(input())
num = list(map(int, input().split()))

for i in range(n):
    res = int(reverse(num[i]))
    if res == 1:
       continue
    flag = isPrime(res)
    if flag == 1:
        print(res, end = " ")


