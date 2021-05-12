'''
문자열과 내장함수
'''

msg = "It is Time"

print(msg.upper())
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg)

print(msg[:2])
print(msg[3:5])
print(len(msg))

for i in range(len(msg)):
    print(msg[i],end = ' ')
print()

for x in msg:
    print(x, end= " ")
print()


for x in msg:
    if x.isupper():
        print(x, end = "")
print()

for x in msg:
    if x.islower():
        print(x, end = "")
print()

for x in msg:
    if x.isalpha():   #isalph() 알파벳만 참
        print(x, end = "")
print()



tmp = "AZ"
for x in tmp:
    print(ord(x)) #ord() 아스키 넘버 출력함수



tmp = "az"
for x in tmp:
    print(ord(x)) #ord() 아스키 넘버 출력함수

tmp = 65
print(chr(tmp))
print(chr(66))



print(msg[:4])



