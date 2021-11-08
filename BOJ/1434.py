import sys

input = sys.stdin.readline

number_of_boxes, number_of_books = map(int, input().split())
boxes = list(map(int,input().split()))
books = list(map(int,input().split()))

box_number = 0
book_number = 0

while book_number < number_of_books and box_number < number_of_boxes:
    if boxes[box_number] >= books[book_number]:
        boxes[box_number] -= books[book_number]
        book_number += 1
    else:
        box_number += 1
print(sum(boxes))
