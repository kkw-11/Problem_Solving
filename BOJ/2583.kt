import java.io.*
import kotlin.Pair as Pair
var row_dir = arrayOf(1,0,-1,0)
var col_dir = arrayOf(0,-1,0,1)

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (m, n, k) = br.readLine().split(' ').map{it.toInt()}
    var matrix = Array(m, {IntArray(n,{0})})
    var checked = Array(m, {IntArray(n,{0})})
    var cnt = 0
    var areas = mutableListOf<Int>()

    for (a in 0..k-1){
        val (x1, y1, x2, y2) = br.readLine().split(' ').map{it.toInt()}
        for (i in y1..(y2-1)){
            for (j in x1..(x2-1)){
                matrix[i][j] = 1
            }
        }
    }

    for (i in 0..m-1){
        for (j in 0..n-1){
            if(matrix[i][j] == 0 && checked[i][j] == 0){
                cnt += 1
                areas.add(BFS(i,j,m,n,matrix, checked))
            }
        }
    }
    areas.sort()
    println(cnt)
    for(a in areas){
        print("$a ")
    }
}

fun BFS(row:Int, col:Int, m:Int, n:Int, matrix:Array<IntArray>, checked:Array<IntArray>):Int{
    var queue = arrayListOf<Pair<Int,Int>>()
    var area = 1
    checked[row][col] = 1
    queue.add(Pair(row,col))

    while(queue.isNotEmpty()){
        val (cur_row, cur_col) = queue.removeAt(0)
        for (k in 0..3){
            val next_row = cur_row + row_dir[k]
            val next_col = cur_col + col_dir[k]
            if ((next_row>=0 && next_row<m) && (next_col>=0 && next_col<n)){
                if (matrix[next_row][next_col] == 0 && checked[next_row][next_col]==0){
                    checked[next_row][next_col] = 1
                    queue.add(Pair(next_row, next_col))
                    area += 1
                }
            }
        }
    }
    return area
}