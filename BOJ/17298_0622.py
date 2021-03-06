import sys
input = sys.stdin.readline

sequence_len = int(input())
sequence = list(map(int,input().split()))
answer = [-1]*sequence_len
stack = [0] #아직 오큰수를 못 찾은 수열의 원소의 인덱스 값을 저장하는 스택, 초기값 0 인덱스

for index in range(1, sequence_len):
    while stack and sequence[stack[-1]] < sequence[index]:
        answer[stack[-1]] = sequence[index]
        stack.pop()
    stack.append(index)
    
print(*answer)




