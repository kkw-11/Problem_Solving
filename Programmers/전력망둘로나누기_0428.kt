import kotlin.math.min
import kotlin.math.abs
class Solution {
    var answer: Int = Int.MAX_VALUE
    var tree = Array(0) {BooleanArray(0)}
    var checked = BooleanArray(0) {false}
    
    fun dfs(cur: Int, n: Int): Int {
        var child = 1
        checked[cur] = true
        for (next in 1..n) {
            if(tree[cur][next] && checked[next] == false){
                child += dfs(next, n)
            }
        }
        answer = min(answer, abs(n - child - child))
        return child
    }

    fun solution(n: Int, wires: Array<IntArray>): Int {
        tree = Array(n+1) {BooleanArray(n+1)}
        checked = BooleanArray(n+1) {false}
        for(wire in wires) {

            tree[wire[0]][wire[1]] = true
            tree[wire[1]][wire[0]] = true
        }

        dfs(2, n)

        return answer
    }
}