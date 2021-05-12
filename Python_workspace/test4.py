'''

반복문 (for, while)

a = range(10) #순차적으로 정수 리스트를 만든다.

print(list(a))

print(a)

a = range(1,11)

print(list(a))



for i in range(1,10):
    print(i)



for i in range(10,0,-2):
    print(i)

i = 1
while i<=10:
    print(i)
    i = i+1

i = 10
while i>0:
    print(i)
    i = i -1

i = 1
while True:
    print(i)
    if(i == 10):
        break
    i += 1

for i in range(1,11):
    if(i%2 == 0):
        continue
    print(i)
    print(i)
'''

for i in range(1,11):
    print(i)
    if i == 15:
        break
else:
    print(11)







    










    
