import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
set_data = {}
for _ in range(n):
    input_value = input().split()
    if len(input_value) > 1:
        operator, n = input_value[0], int(input_value[1])
    else:
        operator = input_value[0]

    if operator == "add":
        set_data[n] = True
    elif operator == "remove":
        if n in set_data:
            del set_data[n]
    elif operator == "check":
        if n in set_data:
            print(1)
        else:
            print(0)
    elif operator == "toggle":
        if n in set_data:
            del set_data[n]
        else:
            set_data[n] = True
    elif operator == "all":
        if len(set_data) == 20:
            continue
        for i in range(1,21):
            set_data[i] = True
    elif operator == "empty":
        set_data = {}
