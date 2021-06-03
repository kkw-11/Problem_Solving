'''
함수 만들기

def add(a,b):
    return a+b

print(add(2,3))


c = add(11,3)
print(c)

add(33,2)



def add(a,b):
    c = a + b
    d = a - b
    return c,d,a


x=add(1,2)
print(x)

print(x[0])
'''

a = [12,13,7,9,19]

def isPrime(a):
    for x in a:
        if x ==1:
            continue
        for i in range(2,x):
            if x % i == 0:
                break
        else:
            print(x)
      
isPrime(a)
