import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int,input().split()))

#def digit_sum(x):
#    digitSum = 0
#    while x:
#        digitSum += x %10
#        x //= 10
#    return digitSum

def digit_sum(x):
    digitSum = 0
    for i in str(x):
        digitSum += int(i)

    return digitSum

max = -1

for i in range(n):
    total = digit_sum(num[i])
    if total > max:
        max = total
        answer = num[i]

print(answer)