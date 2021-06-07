import sys
#sys.stdin = open("input.txt","rt")

str1 = input()
num = ""
res = 0
cnt = 0
for char in str1:
    if char.isdecimal():
        res = res*10 + int(char)

for i in range(1,res+1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)