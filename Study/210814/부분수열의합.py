import sys

res = set()
nums = []

def subSet(depth, sum, n, nums):

    if depth == n:
        res.add(sum)
        return 

    sum += nums[depth]
    subSet(depth+1,sum, n, nums)
    
    sum -= nums[depth]
    subSet(depth+1,sum, n, nums)

#sys.stdin = open("input.txt")
    
n = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().rstrip().split()))

subSet(0,0,n,nums)

res = list(res)
res.sort()
for i in range(len(res)):
    if res[i] != i:
        print(i)
        break
else:
    print(res[-1]+1)
