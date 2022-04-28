import kotlin.math.min
import kotlin.math.abs
class Solution {
    var answer: Int = Int.MAX_VALUE
    var tree = Array(0) {BooleanArray(0)}
    var visited = BooleanArray(0)
    
    # 트리 후위 순회 방식으로 answer 값 갱신 및 자식 노드 수 구하기
    fun childCount(cur: Int, n: Int): Int {
        var ret = 1
        visited[cur] = true
        for (next in 1..n) {
            if(tree[cur][next] && !visited[next]){
                visited[next] = true
                ret += childCount(next, n)
            }
        }
        
        answer = min(answer, abs(n - ret - ret))
        return ret
    }

    fun solution(n: Int, wires: Array<IntArray>): Int {
        tree = Array(n+1) {BooleanArray(n+1)}
        visited = BooleanArray(n+1){false}

        for(wire in wires) {

            tree[wire[0]][wire[1]] = true
            tree[wire[1]][wire[0]] = true
        }

        childCount(2, n)

        return answer
    }
}