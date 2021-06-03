import sys
sys.stdin = open("input.txt","rt")

n = int(input())
lis = list(map(int,input().split()))
cnt = 0
score = 0

for i in range(n):
    if lis[i] == 1:
        cnt += 1
        score += cnt
    else:
        cnt = 0

print(score)

# import sys
# sys.stdin = open("input.txt","rt")

# n = int(input())
# lis = list(map(int,input().split()))
# cnt = 0
# score = 0

# for i in range(n):
#     if lis[i] == 1:
#         cnt += 1
#     else:
#         for j in range(cnt,0,-1):
#             score += j
#         cnt = 0
# else:
#     for j in range(cnt,0,-1):
#         score += j

# print(score)