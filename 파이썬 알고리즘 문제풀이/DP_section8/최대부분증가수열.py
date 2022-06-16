import sys

n = int(input())
nums = list(map(int,input().split(" ")))

answer = [1]*n

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if nums[i] > nums[j]:
            if answer[i] <= answer[j]:
                answer[i] = answer[j] + 1

print(max(answer))