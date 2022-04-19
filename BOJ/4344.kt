import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()

    for (i in 1..n){
        var list = br.readLine().split(' ').map{it.toInt()}
        val avg = (list.sum() - list[0])/list[0]
        var cnt = 0
        for(i in 1..list[0]){
            if (list[i] > avg){
                cnt += 1
            }
        }
        print(String.format("%.3f",(cnt*100/list[0].toDouble())))
        println("%")

        //var a = "%.3f".format((cnt/list[0])*100)
        //print("${a}%\n")
        //print(", ")
        //print("%.3f".format((cnt/list[0])*100)+"%\n")
    }


}