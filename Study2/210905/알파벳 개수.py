import sys

input_data = sys.stdin.readline().rstrip()
answer = [0]*26

for alphabet in input_data:
    answer[ord(alphabet)-97] += 1

print(*answer)
