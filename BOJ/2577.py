# 개선 코드
import sys
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

num = A*B*C
count = [0 for _ in range(10)]

while num:
    count[num%10] += 1
    num //= 10

for i in range(10):
    print(count[i])



## 첫 풀이
# import sys

# sys.stdin = open("input.txt", "rt")

# num1 = int(sys.stdin.readline().rstrip())
# num2 = int(sys.stdin.readline().rstrip())
# num3 = int(sys.stdin.readline().rstrip())

# multyNum = num1 * num2 * num3

# #숫자를 정렬하기 위해 list에 저장하는 방법
# # 문자열로 만들고 int로 매핑하면
# numlist = [int(a) for a in str(multyNum)]

# numlist.sort()
# print(numlist)

# cur = 0

# for i in range(10):
#     cnt = 0
#     for j in range(cur, len(numlist)):
#         if numlist[j] == i:
#             cnt += 1
#         else:
#             break
#     cur = j
#     print(cnt)

