import sys

sys.stdin = open("input.txt","rt")

N, X = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))

print(nums)