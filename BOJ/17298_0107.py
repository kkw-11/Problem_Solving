import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))

stack = [0]
answer = [-1]*n

for i in range(n):
    while len(stack) and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    else:
        stack.append(i)
print(*answer)