import sys
input = sys.stdin.readline

input_data = input().rstrip()

while input_data != '0':
    left = 0
    right = len(input_data)-1
    while left <= right:
        if input_data[left] == input_data[right]:
            left += 1
            right -= 1
        else:
            print('no')
            break
    else:
        print("yes")
    input_data = input().rstrip()