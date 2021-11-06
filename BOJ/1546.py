import sys
n = int(sys.stdin.readline().rstrip())

input_data = list(map(int,sys.stdin.readline().rstrip().split()))
maxData = max(input_data)

for idx, score in enumerate(input_data):
    input_data[idx] = score/maxData*100

print(sum(input_data)/n)