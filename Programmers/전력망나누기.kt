import kotlin.math.*

class Solution {
    fun solution(n: Int, wires: Array<IntArray>): Int {
        var answer: Int = n
        var tree = Array(n+1,{mutableSetOf<Int>()}) 
        
        for (wire in wires){
            tree[wire[0]].add(wire[1])
            tree[wire[1]].add(wire[0])
        }
        
        for (wire in wires){
            tree[wire[0]].remove(wire[1])
            tree[wire[1]].remove(wire[0])
            
            var visited_cnt = DFS(wire[0],tree)
            var result = abs(n - visited_cnt - visited_cnt)
            
            if (result < answer){
                answer = result
            }
            
            tree[wire[0]].add(wire[1])
            tree[wire[1]].add(wire[0])
            
        }
        
        return answer
    }
    
    
    fun DFS(start:Int, tree:Array<MutableSet<Int>>):Int{
        var stack = mutableListOf<Int>(start)
        var checked = mutableSetOf<Int>(start)
        
        while(stack.isNotEmpty()){
            var cur_node = stack.removeAt(stack.size-1)
            
            for(next_node in tree[cur_node]){
                if (!checked.contains(next_node)){
                    stack.add(next_node)
                    checked.add(next_node)
                }
            }
        }
        return checked.size
    }
}