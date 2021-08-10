import sys

n = int(sys.stdin.readline().rstrip())

answer = [1]* n 
info = [[0,0]] * n

for i in range(n):
    weight, height = map(int,sys.stdin.readline().rstrip().split())
    info[i] = [weight, height]


for i in range(n):
    cnt = 0
    for j in range(n):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            cnt +=1
    else:
        answer[i] += cnt
else:
    for k in range(n):
        print(answer[k],end=" ")
