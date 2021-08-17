import sys

#sys.stdin = open("input.txt")

n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
res = [-1]*n
stack = []

stack.append(0)

for index in range(1,n):
    while stack and nums[stack[-1]] < nums[index]:
        res[stack[-1]] = nums[index]
        stack.pop()
    stack.append(index)

print(*res)
