'''
반복문을 이용한 문제풀이\
 1) 1부터 N까지 홀수 출려하기
 2) 1부터 N까지의 합 구하기
 3) N의 약수 출력하기


print("1)")
N = int(input())


for i in range(1,N+1):
    if(i%2 == 1):
        print(i)
print("2)")

N = int(input())
sum = 0
for i in range(1,N+1):
    sum += i

else:
    print(sum)
'''

print("3)")
N = int(input())

for i in range(1,N+1):
    if N % i== 0:
        print(i, end=" ")
        





