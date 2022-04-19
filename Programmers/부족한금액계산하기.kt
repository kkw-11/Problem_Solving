class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        var answer: Long = -1
        var total: Int = 0
        for(i in 1..count){
            total += price*i
        }
        
        if (total >= money){
            return (total-money).toLong()
        }
        else{
            return 0
        }
        
        return answer
    }
}