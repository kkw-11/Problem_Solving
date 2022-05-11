import sys

n = int(input())

find_num = int(input())

table = [[0]*n for _ in range(n)]
dir_row = [-1,0,1,0]
dir_col = [0,1,0,-1]
whar_dir = 0
move_cnt = 1
cur_row = n//2
cur_col = cur_row
cur_num = 1
while cur_num < n**2:
    for move_cnt in range(1,n-1):
        for _ in range(2):
            for _ in range(move_cnt):
                table[cur_row][cur_col] = cur_num
                if cur_num == find_num:
                    answer = (cur_row,cur_col)
                cur_row += dir_row[whar_dir]
                cur_col += dir_col[whar_dir]
                cur_num += 1
            whar_dir = (whar_dir+1)%4
        move_cnt += 1
    else:
        for _ in range(3):
            for _ in range(move_cnt):
                table[cur_row][cur_col] = cur_num
                if cur_num == find_num:
                    answer = (cur_row,cur_col)
                cur_row += dir_row[whar_dir]
                cur_col += dir_col[whar_dir]
                cur_num += 1
            whar_dir = (whar_dir+1)%4
        else:
            table[cur_row][cur_col] = cur_num
            if cur_num == find_num:
                answer = (cur_row,cur_col)

for row in table:
    print(*row)
print(answer[0]+1,end=" ")
print(answer[1]+1)


