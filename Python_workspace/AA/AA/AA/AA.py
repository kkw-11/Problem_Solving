import sys

sys.stdin = open("input.txt","rt")
n,m = map(int,input().split())
num = list(map(int,input().split()))

sum = 0
cnt = 0
lp = 0
rp = 1
sum += num[lp]
#while lp < n:
#    if sum < m:
#        if rp == n:
#            break
#        sum+=num[rp]
#        rp += 1
#    elif sum == m:
#        cnt += 1
#        sum -= num[lp]
#        lp += 1
#    else:
#        sum -= num[lp]
#        lp += 1


for i in range(len(num)):
    sum += num[i]
    if sum == m:
        cnt += 1
        sum = 0
        continue
    elif sum < m:
        for j in range(i+1,len(num)):
            sum += num[j]
            if sum == m:
                cnt += 1
                sum = 0
                break
            elif sum > m:
                sum = 0
                break
    else:
        sum = 0
print(cnt)
