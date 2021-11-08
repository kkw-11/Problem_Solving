import sys

input = sys.stdin.readline
screen, basket_size = map(int,input().split())

number_of_apples = int(input())
position_info = []

for _ in range(number_of_apples):
    position_info.append(int(input()))
basket_left = 1
basket_right = basket_left + basket_size

move = 0

for apple_position in position_info:
    if apple_position >= basket_left and apple_position < basket_right:
        continue
    else: #apple_position < basket_left or apple_position >= basket_right
        if apple_position < basket_left:
            cur_move = basket_left - apple_position
            basket_left = basket_left - cur_move
            basket_right = basket_right - cur_move
            move += cur_move
        elif apple_position >= basket_right:
            cur_move = abs(apple_position + 1 - basket_right)
            basket_left = basket_left + cur_move
            basket_right = basket_right + cur_move 
            move += cur_move

print(move)