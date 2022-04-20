class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        var answer: Int = 0
        var max_width = 0
        var max_height = 0
        for(size in sizes){
            if (size[0] < size[1]){
                var temp = size[0]
                size[0]=size[1]
                size[1] = temp
            }
            if (max_width<size[0]){
                max_width =size[0]
            }
            if(max_height<size[1]){
                max_height = size[1]
            }
        }
       
        
        return max_width*max_height
    }
}