import sys

def go(row,col, number, depth):
    if depth == 5:
        answer.add(number)
    else:
        for i in range(4):
            new_row = row + dir_row[i]
            new_col = col + dir_col[i]
            if new_row >=0 and new_row<5 and new_col >=0 and new_col <5:
                go(new_row,new_col,number+graph[new_row][new_col],depth+1)

input = sys.stdin.readline

answer = set()
dir_col = [-1,1,0,0]
dir_row = [0,0,-1,1]
graph = []

# Adjacency matrix graph
for _ in range(5):
    graph.append(input().split())

for row in range(5):
    for col in range(5):
        go(row,col,graph[row][col],0)

print(len(answer))