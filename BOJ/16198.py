import sys

input = sys.stdin.readline

def DFS(total):
    global answer
    if len(nums) <= 2:
        answer = max(answer,total)
        return
    else:
        for i in range(1,len(nums)-1):
            weight = nums[i-1]*nums[i+1]
            temp = nums[i]
            nums.pop(i)
            DFS(total+weight)
            nums.insert(i,temp)

n = int(input())
nums = list(map(int,input().split()))

answer = 0
DFS(0)

print(answer)