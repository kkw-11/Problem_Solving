def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
   
    for move in moves:
        for i in range(n):
            if board[i][move-1] == 0:
                continue
            else:
                
                if len(basket) >= 1 and basket[-1] == board[i][move-1]:
                    
                    basket.pop()
                    answer += 2
                    
                else:
                    basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
    return answer