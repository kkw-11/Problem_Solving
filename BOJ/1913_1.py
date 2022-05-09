import sys

n = int(input())
find_num = int(input())

table = [[0]*n for _ in range(n)]
dir_row = [-1,0,1,0]
dir_col = [0,1,0,-1]
cur_row = n//2
cur_col = cur_row
cur_num = 1
dir = 0
dir_cnt = 1

while cur_num < n**2:
    for i in range(1,n):
        if i <= n-2:
            for _ in range(2):
                for _ in range(i):
                    table[cur_row][cur_col] = cur_num
                    if cur_num == find_num:
                        answer = (cur_row+1,cur_col+1)
                    cur_num += 1
                    cur_row += dir_row[dir]
                    cur_col += dir_col[dir]
                dir = (dir + 1)%4
            dir_cnt += 1
        else:
            for _ in range(3):
                for _ in range(i):
                    table[cur_row][cur_col] = cur_num
                    if cur_num == find_num:
                        answer = (cur_row+1,cur_col+1)
                    cur_num += 1
                    cur_row += dir_row[dir]
                    cur_col += dir_col[dir]
                dir = (dir + 1)%4
            table[cur_row][cur_col] = cur_num
            if cur_num == find_num:
                answer = (cur_row+1,cur_col+1)
for row in table:
    print(*row)
print(answer[0],end=" ")
print(answer[1])