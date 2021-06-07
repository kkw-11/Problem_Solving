import sys
#sys.stdin = open("input.txt","rt")

str1 = input()
num = ""
cnt = 0
for char in str1:
    if ord(char)>= 48 and ord(char)<=57:
        num += char

num = int(num)

for i in range(1,num+1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)