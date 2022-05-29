import sys

input = sys.stdin.readline
n = int(input())
arr = [0]
arr.extend(map(int,input().split()))

answer = 0
dy_LIS = [1]*(n+1)
for i in range(2,n+1):
    max_len = 1
    for j in range(i-1,0,-1):
        if arr[i] > arr[j]: #나(j)보다 작은 수 중에서 부분 증가 수열 길이가 가장 긴 값
            if max_len < dy_LIS[j]+1:
                max_len = dy_LIS[j]+1
            if answer == dy_LIS[j]:
                break
    dy_LIS[i] = max_len
    if answer < dy_LIS[i]:
        answer = dy_LIS[i]

print(answer)