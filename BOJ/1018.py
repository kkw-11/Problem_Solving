import sys

n, m = map(int,input().split())
table = [[] for _ in range(n)]

for row in range(n):
    col = input().rstrip()
    for ch in col:
        table[row].append(ch)

min_cnt = 65
for start_row in range(0,n-7):
    for start_col in range(0,m-7):
        cnt = 0
        start_color = table[start_row][start_col]

        # 시작 행 포함 짝수번 증가한 행
        for row in range(start_row,start_row+7,2):#start_row start_row+2 start_row+4 start_row+6
            # 기준값과 같은 색칸이여야 하는 곳
            for col in range(start_col,start_col+7,2):
                if table[row][col] != start_color:
                    cnt += 1
            # 기준값과 다른 색칸이여야 하는 곳
            for col in range(start_col+1,start_col+8,2):
                if table[row][col] == start_color:
                    cnt += 1
        # 시작 행+1부터 짝수번 증가한 행            
        for row in range(start_row+1,start_row+8,2):
            for col in range(start_col,start_col+7,2):
                if table[row][col] == start_color:
                    cnt += 1
            for col in range(start_col+1, start_col+8,2):
                if table[row][col] != start_color:
                    cnt += 1
        cnt = min(cnt,64-cnt)

        min_cnt = min(cnt,min_cnt)
print(min_cnt)