import sys

def isPrime(n):
    if n == 1:
        return False

    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    
    return True

n = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().rstrip().split()))
cnt = 0
for i in range(n):
    if isPrime(nums[i]):
        cnt += 1
print(cnt)
