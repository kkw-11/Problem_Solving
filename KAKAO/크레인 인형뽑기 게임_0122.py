def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
   
    for col in moves:
        for row in range(n):
            if board[row][col-1] == 0:
                continue
            else:
                basket.append(board[row][col-1]) 
                board[row][col-1] = 0
                
                if len(basket) >= 2 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
                break
                
    return answer