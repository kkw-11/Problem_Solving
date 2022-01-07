import sys
input = sys.stdin.readline

input_data = input().rstrip()

input_data_list = list(input_data)

number_dict = {"A":2,"B":2,"C":2,
               "D":3,"E":3,"F":3,
               "G":4,"H":4,"I":4,
               "J":5,"K":5,"L":5,
               "M":6,"N":6,"O":6,
               "P":7,"Q":7,"R":7,"S":7,
               "T":8,"U":8,"V":8,
               "W":9,"X":9,"Y":9,"Z":9
               }
total = 0
input_data_len = len(input_data_list)
for ch in input_data_list:
    total += (number_dict[ch] -1)

print(total + 2*input_data_len)