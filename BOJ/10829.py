import sys

input = sys.stdin.readline

n = int(input())

answer = []
while n:
    answer.append(n % 2)
    n //= 2
for index in range(len(answer)-1,-1,-1):
    print(answer[index],end="")
