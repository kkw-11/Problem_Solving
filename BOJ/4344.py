import sys
sys.stdin = open('input.txt',"rt")

n = int(sys.stdin.readline().rstrip())


for i in range(n):
    input_data = list(map(int,sys.stdin.readline().rstrip().split()))
    avg = sum(input_data[1:]) / input_data[0]
    cnt = 0
    for j in range(1,input_data[0]+1):
        if input_data[j] > avg:
            cnt += 1
    else:
        rate = round(100*cnt/input_data[0],3)
        print(f"{rate:.3f}%")