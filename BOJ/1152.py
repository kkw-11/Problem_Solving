import sys
input = sys.stdin.readline

input_number = int(input())
cur_box_number = [0 for _ in range(10)]
while input_number != 0:
    number = input_number % 10
    input_number = input_number//10

    if number == 6:
        if cur_box_number[6] <= cur_box_number[9]:
            cur_box_number[6] += 1
        elif cur_box_number[6] > cur_box_number[9]:
            cur_box_number[9] += 1
    elif number == 9:
        if cur_box_number[9] <= cur_box_number[6]:
            cur_box_number[9] += 1
        elif cur_box_number[9] > cur_box_number[6]:
            cur_box_number[6] += 1
    else:
        cur_box_number[number] += 1
print(max(cur_box_number))