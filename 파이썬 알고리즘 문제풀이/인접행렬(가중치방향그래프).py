import sys

sys.stdin = open("input.txt","rt")

n, m = map(int, input().split())

matrix = [[0]*n for _ in range(n)]

for _ in range(m):
    row, col, weight = map(int,input().split())
    matrix[row-1][col-1] = weight

for mat in matrix:
    for elem in mat:
        print(elem, end = ' ')
    else:
        print()
