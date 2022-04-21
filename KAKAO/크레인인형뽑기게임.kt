class Solution {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0
        var basket = mutableListOf<Int>()
        for(move in moves){
            for (row in 0..board.size-1){
				if (board[row][move-1] != 0){
                    basket.add(board[row][move-1])
                    board[row][move-1] = 0
                  	if(basket.size >=2){
                        if(basket[basket.size-1] == basket[basket.size-2]){
                            basket.removeAt(basket.size-1)
                            basket.removeAt(basket.size-1)
                            answer += 2
                        }
                    }
                    break
                }              
            }
        }
        return answer
    }
}