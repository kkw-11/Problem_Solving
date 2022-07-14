import sys
input = sys.stdin.readline

sequence_length = int(input())
sequence = list(map(int,input().split()))
answer = [-1]*sequence_length

stack = [] #아직 오큰수를 찾지 못한 수열의 원소의 인덱스 값을 저장하는 스택
for index in range(sequence_length):
    while stack and sequence[stack[-1]] < sequence[index]:
        answer[stack[-1]] = sequence[index]
        stack.pop()
    stack.append(index)
    
print(*answer)




