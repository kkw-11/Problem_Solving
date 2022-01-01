num, base = map(int, input().strip().split(' '))
answer = 0
i = 0
while num:
    answer += ((num % 10)*(base**i))
    i += 1
    num //= 10
print(answer)

