import sys

input = sys.stdin.readline

start = int(input())
end = int(input())
total = 0
min_answer = float("inf")

for num in range(10000*10000 + 1):
    if num*num >= start and num*num <= end:
        if min_answer > num*num:
            min_answer = num*num
        total += num*num
    elif num*num > end:
        break
if total == 0 and min_answer == float("inf"):
    print(-1)
else:
    print(total)
    print(min_answer)