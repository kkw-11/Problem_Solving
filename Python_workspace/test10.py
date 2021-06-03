'''
2차원 리스트 생성과 접근
'''

#a = [1]*3
#a.append(33)
#print(a)

a = [[0]*4 for _ in range(3)] #0으로 초기화된 2행 4열 짜리 리스트 생성

print(a)


a[0][1] = 33


print(a)

for x in a:
    for y in x:
        print(y, end = " ")
    print()



for x in a:
    print(x)


