import java.io.*
import kotlin.Pair as Pair

var row_dir = arrayOf(1,0,-1,0)
var col_dir = arrayOf(0,-1,0,1)
var cur_sheeps = 0
var cur_worlfs = 0
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (r, c) = br.readLine().split(' ').map{it.toInt()}
    var matrix = Array(r, { mutableListOf<Char>() })
    val checked = Array(r,{BooleanArray(c,{false})})
    var answer_sheeps = 0
    var answer_wolfs = 0


    for(i in 0..r-1){
        var tocken = br.readLine().toList()
        for (j in 0..c-1){
            matrix[i].add(tocken[j])
        }
    }

    for(row in 0..r-1){
        for(col in 0..c-1){
            cur_sheeps = 0
            cur_worlfs = 0
            if (matrix[row][col] != '#' && checked[row][col] == false){
                BFS(row, col, r, c, matrix, checked)
                if (cur_worlfs < cur_sheeps){
                    answer_sheeps += cur_sheeps
                }
                else{
                    answer_wolfs += cur_worlfs
                }
            }
        }
    }
    print("${answer_sheeps} ${answer_wolfs}")
}


fun BFS(row:Int, col:Int, r:Int, c:Int, matrix:Array<MutableList<Char>>, checked:Array<BooleanArray>):Unit{
    var queue = arrayListOf<Pair<Int,Int>>()
    var area = 1
    checked[row][col] = true
    queue.add(Pair(row,col))

    if (matrix[row][col] =='v'){
        cur_worlfs += 1
    }
    else if(matrix[row][col] == 'o'){
        cur_sheeps += 1

    }

    while(queue.isNotEmpty()){
        val (cur_row, cur_col) = queue.removeAt(0)
        for (k in 0..3){
            val next_row = cur_row + row_dir[k]
            val next_col = cur_col + col_dir[k]
            if ((next_row>=0 && next_row<r) && (next_col>=0 && next_col<c)){
                if (matrix[next_row][next_col] != '#'  && checked[next_row][next_col] == false){
                    checked[next_row][next_col] = true
                    queue.add(Pair(next_row, next_col))
                    if (matrix[next_row][next_col] == 'v'){
                        cur_worlfs += 1
                    }else if(matrix[next_row][next_col] == 'o'){
                        cur_sheeps += 1

                    }
                }
            }
        }

    }
}
