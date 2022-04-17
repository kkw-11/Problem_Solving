from collections import deque

def solution(maps):
    cnt = 1
    
    col = len(maps[0])
    row = len(maps)
    
    dir_row = [1,-1,0,0]
    dir_col = [0,0,1,-1]
    start_row = 0
    start_col = 0
    checked = [[False]*col for _ in range(row)]
    checked[start_row][start_col] = True


    q = deque()
    q.append((start_row,start_col,cnt))
    
    while q:
        cur_row, cur_col, cnt = q.popleft()
        if cur_row == row-1 and cur_col == col-1:
            return cnt
        
        for dir in range(4):
            next_row = cur_row + dir_row[dir]
            next_col = cur_col + dir_col[dir]
            if (next_row >= 0 and next_row < row and next_col >= 0 and next_col < col) and maps[next_row][next_col] == 1:
                if not checked[next_row][next_col]:
                    checked[next_row][next_col] = True
                    q.append((next_row,next_col, cnt+1))
                
    else:
        return -1
            