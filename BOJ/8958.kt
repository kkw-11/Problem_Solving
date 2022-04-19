import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    for(i in 1..n){
        var answer:String = br.readLine()
        var cnt = 0
        var total = 0
        for (j in 0..answer.length-1) {
            if (answer[j] == 'O'){
                cnt += 1
                total += cnt
            }
            else{
                cnt = 0
            }
        }
        println(total)
    }

}