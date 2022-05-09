import sys
input = sys.stdin.readline

num = input().rstrip()
n = len(num)
num = int(num)
total = 0

for i in range(1,n):
    total += ( 9*int('1'*(i)) - 10**(i-1)  +1)*(i)
total += (num-10**(n-1)+1)*n
print(total)