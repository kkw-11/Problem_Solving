import sys

input = sys.stdin.readline

n = int(input())
numbers = []
temp_numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

if sum(numbers)//n >= 0:
    avg = int((sum(numbers)/n + 0.5))
else:
    avg = int((sum(numbers)/n - 0.5))

mid = numbers[n//2]

# 최빈값
start = 0
cur = 0
while cur < n:
    cnt = 1
    for next in range(cur+1, n):
        if numbers[cur] == numbers[next]:
            cnt += 1
            cur = next
        else:
            temp_numbers.append((cnt, numbers[cur]))
            break
    cur += 1
else:
    temp_numbers.append((cnt, numbers[n-1]))

temp_numbers.sort(reverse=True)

if len(temp_numbers) == 1:
    frequency = temp_numbers[0][1]
else:
    if temp_numbers[0][0] != temp_numbers[1][0]:
        frequency = temp_numbers[0][1]
    else:
        for index in range((len(temp_numbers)-1)):
            if temp_numbers[index][0] != temp_numbers[index+1][0]:
                frequency = temp_numbers[index-1][1]
                break
        else: # 빈출값이 전부 다 같을 때
            frequency = temp_numbers[index][1]

number_range = numbers[-1] - numbers[0]

print(avg)
print(mid)
print(frequency)
print(number_range)