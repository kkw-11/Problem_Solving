import sys

sum = 0
for i in range(3):
    input_data = int(input())

    if input_data < 40:
        sum += 40
    else:
        sum += input_data
print(sum//5)
