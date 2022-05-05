import kotlin.math.min
import kotlin.math.abs
class Solution {
    var answer: Int = Int.MAX_VALUE
    var tree = Array(0) {BooleanArray(0)}

    fun dfs(cur: Int, n: Int): Int {
        var child_me = 1

        for (next in 1..n) {
            if(tree[cur][next]){
                tree[cur][next] = false
                tree[next][cur] = false
                child_me += dfs(next, n)
            }
        }

        answer = min(answer, abs(n - child_me - child_me))
        return child_me
    }

    fun solution(n: Int, wires: Array<IntArray>): Int {
        tree = Array(n+1) {BooleanArray(n+1)}

        for(wire in wires) {

            tree[wire[0]][wire[1]] = true
            tree[wire[1]][wire[0]] = true
        }

        dfs(2, n)

        return answer
    }
}ㅎ