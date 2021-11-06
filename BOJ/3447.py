import sys

while True:
    try:
        input_data = input()
        while "BUG" in input_data:
            for i in range(len(input_data)-2):
                if input_data[i:i+3] == "BUG":
                    input_data = input_data[:i] + input_data[i+3:]
                    break
        if "BUG" not in input_data:
            print(input_data)

    except:
        break
