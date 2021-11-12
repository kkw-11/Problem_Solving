import sys

input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    nums = list(map(int,input().split()))
    nums.sort()
    print(nums[7])