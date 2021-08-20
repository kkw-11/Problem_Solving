import sys

start, end = map(int, sys.stdin.readline().rstrip().split())

primeCheck = [True]*(end+1)
primeCheck[0] = False
primeCheck[1] = False

for i in range(2,end+1):
    for j in range(i+i,end+1,i):
        primeCheck[j] = False

for k in range(start, end+1):
    if primeCheck[k]:
        print(k)