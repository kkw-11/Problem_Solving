import sys
#sys.stdin = open('input.txt',"rt")

n = int(sys.stdin.readline().rstrip())
curScore = 0
answer = 0

for i in range(n):
    input_data = sys.stdin.readline().rstrip()
    curScore = 0
    answer = 0
    for ch in input_data:
        if ch == 'O':
            curScore += 1
            answer += curScore
        else:
            curScore = 0
    print(answer)
