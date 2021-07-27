import sys

input_data = sys.stdin.readline().rstrip()

answer = [-1]*26

for i in range(len(input_data)):
    if answer[ord(input_data[i])-97] == -1 :
        answer[ord(input_data[i])-97] = i

for elem in answer:
    print(elem,end=" ")
