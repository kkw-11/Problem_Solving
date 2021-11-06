import sys
import math

min_burger = math.inf
min_drink = math.inf

for i in range(3):
    input_data = int(input())

    if input_data < min_burger:
        min_burger = input_data

for i in range(2):
    input_data = int(input())

    if input_data < min_drink:
        min_drink = input_data

print(min_burger + min_drink - 50)