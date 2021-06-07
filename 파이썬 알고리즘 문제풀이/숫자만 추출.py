import sys
#sys.stdin = open("input.txt","rt")

str1 = input()
num = ""
res = 0
cnt = 0
for char in str1:
    if char.isdecimal(): #ord(char)>=48 and ord(char)<=57 아스키 코드로 비교
        res = res*10 + int(char) #C언어에서 스타일 orc(char)-48을 해주면 문자형 숫자를 진짜 숫자로 변환가능

for i in range(1,res+1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)

# import sys
# #sys.stdin = open("input.txt","rt")

# str1 = input()
# num = ""
# cnt = 0
# for char in str1:
#     if ord(char)>= 48 and ord(char)<=57:
#         num += char

# num = int(num)

# for i in range(1,num+1):
#     if num % i == 0:
#         cnt += 1

# print(num)
# print(cnt)