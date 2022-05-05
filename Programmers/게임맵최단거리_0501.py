from collections import deque
answer = float("inf")
dir_row = [1,-1,0,0]
dir_col = [0,0,1,-1]
def solution(maps):
    cnt = 1
    
    col = len(maps[0])
    row = len(maps)
    
    start_row = 0
    start_col = 0
    checked = [[False]*col for _ in range(row)]
    checked[start_row][start_col] = True
    
    DFS(1,0,0,maps,checked,row,col)
    
    if answer == float("inf"):
        return -1
    else:
        return answer
        

def DFS(cnt,cur_row,cur_col,maps,checked,row,col):
    global answer, dir_row, dir_col
    if cur_row == row-1 and cur_col == col-1:
        if answer > cnt:
            answer = cnt
        
    else:
        for dir in range(4):
            next_row = cur_row + dir_row[dir]
            next_col = cur_col + dir_col[dir]
            if next_row>=0 and next_row<row and next_col>=0 and next_col<col:
                if not checked[next_row][next_col] and maps[next_row][next_col]==1:
                    checked[cur_row][cur_col] = True
                    
                    DFS(cnt+1,next_row,next_col,maps,checked,row,col)
                    checked[cur_row][cur_col] = False