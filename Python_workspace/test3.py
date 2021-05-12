'''
변수입력과 연산자
'''

'''
a,b = input("숫자를 입력하세요: ").split()
a= int(a)
b= int(b)

print(a,b)
print(type(a))

c = a+b
print(type(c))

print(a+b)


a,b = map(int,input("숫자를 입력하세요: ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫
print(a%b) #나머지
print(a**b) #거듭제곱
'''

'''

a= 4.3
b= 5
c = a+b
print(type(a))
print(type(b))
print(type(c))


조건문(분기,중첩)



x = 5
if x != 7:
    print("Lucky")
    print("ㅋㅋ")

x = 12
if x>=10:
    if x%2 == 1:
        print("10이상의 홀수")

x = 1
if x>0:
    if x<10 :
        print("10보다 작은 자연수")



x= 2
if 0< x<10:
    print("10보다 작은 자연수")



x = 10
if x>0:
    print("양수")
else:
    print("음수")

'''

x = 50
if x>=90:
    print("A")
elif x>=80:
    print("B")
elif x>=70:
    print("C")
elif x>=60:
    print("D")
else:
    print("F")





