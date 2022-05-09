import sys
input = sys.stdin.readline

n = int(input())

find_num = int(input())

cur_row = n//2
cur_col = cur_row

dir_row = [-1,0,1,0]
dir_col = [0,1,0,-1]
table = [[0]*n for _ in range(n)]

cur_num = 1
dir = 0
dir_cnt = 1
while cur_num != n**2:
    
    if dir_cnt<n-1:
        for _ in range(2):
            for _ in range(dir_cnt):
                if cur_num == find_num:
                    answer = (cur_row+1,cur_col+1)
                table[cur_row][cur_col] = cur_num
                cur_num += 1

                cur_row = dir_row[dir%4]+cur_row
                cur_col = dir_col[dir%4]+cur_col
            dir += 1
        dir_cnt += 1
    else:
        for _ in range(3):
            for _ in range(dir_cnt):
                if cur_num == find_num:
                    answer = (cur_row+1,cur_col+1)
                table[cur_row][cur_col] = cur_num 
                cur_num += 1

                cur_row = dir_row[dir%4]+cur_row
                cur_col = dir_col[dir%4]+cur_col
            dir += 1

        table[cur_row][cur_col] = cur_num 
        if cur_num == find_num:
            answer = (cur_row+1,cur_col+1)

for row in table:
    print(*row)
print(answer[0],end=" ")
print(answer[1])