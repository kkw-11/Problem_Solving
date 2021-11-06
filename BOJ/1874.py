import sys

sys.stdin = open("input.txt")

n = int(sys.stdin.readline())

seq = []
stack = []
answer = []
seqPoint = 0
curInNum = 1
flag = True

for i in range(n):
    a = int(sys.stdin.readline())
    seq.append(a)

while seqPoint < n:

    if not stack:
        stack.append(curInNum)
        curInNum += 1
        answer.append("+")

    if stack[-1] < seq[seqPoint]:
        temp = curInNum

        for i in range(temp ,seq[seqPoint] +1 ):
            stack.append(i)
            answer.append("+")
        else:
            i += 1
            curInNum = i
    elif stack[-1] == seq[seqPoint]:
        stack.pop()
        answer.append("-")
        seqPoint += 1
    elif  stack[-1] > seq[seqPoint]:
        flag = False
        break

if flag:
    for i in range(len(answer)):
        print(answer[i])
else:
    print("NO")
