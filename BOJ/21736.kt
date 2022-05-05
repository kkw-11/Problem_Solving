import java.io.*
import kotlin.Pair as Pair

var row_dir = arrayOf(1,0,-1,0)
var col_dir = arrayOf(0,-1,0,1)
var start_row = 0
var start_col = 0

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = br.readLine().split(' ').map { it.toInt() }
    var campusMap:Array<MutableList<Char>> = Array(n, { mutableListOf<Char>() })
    val checked = Array(n, { BooleanArray(m, { false }) })
    var friends = 0

    for(i in 0..n-1){
        var tocken = br.readLine().toList()
        for (j in 0..m-1){
            campusMap[i].add(tocken[j])
            if (tocken[j] == 'I'){
                start_row = i
                start_col = j
            }
        }
    }
    friends = BFS(start_row,start_col,checked,campusMap,n,m)
    if(friends>0)
        print(friends)
    else if (friends == 0)
        print("TT")
}

fun BFS(start_row:Int, start_col:Int, checked:Array<BooleanArray>, campusMap:Array<MutableList<Char>>,n:Int,m:Int ):Int{
    var friends  = 0
    var q = arrayListOf<Pair<Int,Int>>(Pair(start_row,start_col))
    checked[start_row][start_col] = true

    while(q.isNotEmpty()){
        val (cur_row, cur_col) = q.removeAt(0)

        for(dir in 0..3){
            val next_row = cur_row + row_dir[dir]
            val next_col = cur_col + col_dir[dir]

            if((next_row>=0 && next_row<n) && (next_col>=0 && next_col<m)){
                if(checked[next_row][next_col] == false && campusMap[next_row][next_col] != 'X'){
                    if (campusMap[next_row][next_col] == 'P') friends += 1

                    checked[next_row][next_col] = true
                    q.add(Pair(next_row,next_col))
                }
            }
        }
    }
    return friends
}