import sys

input = sys.stdin.readline

start, end = map(int,input().split())

seq = [0]
flag = False

for index in range(1, end+1):
    for _ in range(index):
        seq.append(index)
        if len(seq) == end + 1:
            flag = True
            break
    if flag:
        break

print(sum(seq[start:end+1]))