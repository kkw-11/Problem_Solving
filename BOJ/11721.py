import sys

input_data = input()

string_len = len(input_data)
last_line = (string_len//10) + 1
start = 0
end = 10

for line in range(last_line):
    if line != last_line:
        print(input_data[start:end])
        start += 10
        end += 10
    else:
        print(input_data[start:string_len])