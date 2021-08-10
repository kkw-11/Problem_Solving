import sys
#sys.stdin = open("input.txt")

res = 0
n, m = map(int,sys.stdin.readline().rstrip().split())

subjectMile = [0]*n


for i in range(n):
    p, l = map(int,sys.stdin.readline().rstrip().split())
    
    subjects = list(map(int,sys.stdin.readline().rstrip().split()))
    if p < l:
        subjectMile[i] = 1
    else:
        subjects.sort()
        subjectMile[i] = subjects[-l]

subjectMile.sort()

for i in range(n):
    if subjectMile[i] <= m:
        res += 1
        m -= subjectMile[i]
    else:
        break

print(res)