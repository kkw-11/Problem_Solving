n = int(input())

fibo = [None]*(n+1)
fibo[0] = 0
fibo[1] = 1

if n == 1:
    print(fibo[1])
else:
    for i in range(n-1):
        fibo[i+2] = fibo[i] + fibo[i+1]
    print(fibo[n])