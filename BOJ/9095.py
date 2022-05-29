import sys

input = sys.stdin.readline
t = int(input())
dy = [0]*(12)
dy[1] = 1
dy[2] = 2
dy[3] = 4
max_n = 0
test_n = []
for _ in range(t):
    input_data = int(input())
    test_n.append(input_data)
    if max_n < input_data:
        max_n = input_data
for n in range(4,max_n+1):
    dy[n] = dy[n-1] + dy[n-2] + dy[n-3]
for n in test_n:
    print(dy[n])