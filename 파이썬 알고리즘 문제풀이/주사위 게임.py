import sys

#sys.stdin = open("input.txt","rt")

n = int(input())

maxMoney = -1
for i in range(n):
    a,b,c = map(int,input().split())

    if a==b and b==c:
        money = 10000 + a*1000
    elif a==b or a==c: # b,c가 같아서 세개가 같은 경우는 없다. 무조건 두개가 같은데 이유는 첫 if에서 걸려졌기 때문 여기서 첫번째와 두번째 or 첫번째와 세번째이다.
        money = 1000 + a*100
    elif b==c:   # 두 개가 같은 경우중에 두 번째와 세 번째가 같은 경우다.
        money = 1000 + b*100
    else:
        maxNum = max(a,b,c)
        money = maxNum*100

    if money > maxMoney:
        maxMoney = money

print(maxMoney)
## 리패토링 전 코드
# import sys

# #sys.stdin = open("input.txt","rt")

# n = int(input())

# money = [0]*n

# for i in range(n):
#     a, b, c = map(int,input().split())
#     if a == b and b ==c:
#         money[i] = 10000 + a*1000
#     elif (a==b and b!=c) or (a==c and a!=b) or (b==c and a!=b):
#         if a==b:
#             money[i] = 1000 + a*100
#         elif a ==c:
#             money[i] = 1000 + a*100
#         elif b==c:
#             money[i] = 1000 + b*100
#     elif a !=b and b!=c and a!=c:
#         maxNum = max(a,b,c)
#         money[i] = maxNum*100
    

# print(max(money))

