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
a= 4.3
b= 5
c = a+b
print(type(a))
print(type(b))
print(type(c))
