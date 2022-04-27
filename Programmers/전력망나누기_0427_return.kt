import kotlin.math.*

class Solution {
    var visited = Array(0,{false})
    
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
            
            var visited_cnt = 0
            visited = Array(n+1,{false})
            visited_cnt = DFS(wire[0],tree)
            var result = abs(n - visited_cnt - visited_cnt)
            
            if (result < answer){
                answer = result
            }
            
            tree[wire[0]].add(wire[1])
            tree[wire[1]].add(wire[0])
            
        }
        
        return answer
    }
    
    
    fun DFS(cur_node:Int, tree:Array<MutableSet<Int>>):Int{
        var visited_cnt = 1
        
        visited[cur_node] = true
        
        for (node in tree[cur_node]){
            if (!visited[node]){
                visited[node] = true
                visited_cnt += DFS(node,tree)
            }
        }
       return visited_cnt
    }
}