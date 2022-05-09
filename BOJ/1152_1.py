import sys
input = sys.stdin.readline

input_number = int(input())
plastic_nums = [0 for _ in range(10)]
while input_number != 0:
    number = input_number % 10
    input_number = input_number//10
    plastic_nums[number] += 1

plastic_nums[6] = (plastic_nums[6] + plastic_nums[9] + 1)//2
plastic_nums[9] = plastic_nums[6]
print(max(plastic_nums))


