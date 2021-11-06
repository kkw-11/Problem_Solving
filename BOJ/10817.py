import sys

nums = list(map(int,sys.stdin.readline().rstrip().split()))
nums.sort()
print(nums[1])
