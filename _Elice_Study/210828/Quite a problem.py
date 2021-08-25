import sys

while True:
    try:
        input_data = input().lower()
        if "problem" in input_data:
            print("yes")
        else:
            print("no")
    except:
        break
