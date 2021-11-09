import sys

input = sys.stdin.readline
leftmost = 1

screen, basket_size = map(int,input().split())

number_of_apples = int(input())
basket_left = leftmost
basket_right = leftmost + basket_size - 1
move = 0

for _ in range(number_of_apples):
    apple_position = int(input())

    if basket_left <= apple_position <= basket_right: 
        continue
    else: 
        if apple_position < basket_left:
            cur_move = basket_left - apple_position
            basket_left = basket_left - cur_move
            basket_right = basket_right - cur_move
            move += cur_move
        elif apple_position > basket_right:
            cur_move = apple_position - basket_right
            basket_left = basket_left + cur_move
            basket_right = basket_right + cur_move 
            move += cur_move
print(move)