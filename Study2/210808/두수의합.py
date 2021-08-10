# https://www.acmicpc.net/problem/3273

import sys

n = int(sys.stdin.readline().rstrip())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline().rstrip())

answer = 0
left, right = 0, n-1

while left < right:
    temp = numbers[left] + numbers[right]

    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
        
print(answer)


## 다른 풀이
# n=int(input())
# a = {*map(int, input().split())}
# x=int(input())
# #print(a)

# count=sum((x-i in a) for i in a)//2

# print(count)