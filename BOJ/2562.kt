import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var max_data = -9999
    var cnt = 0
    for (i in 1..9){
        val data = br.readLine().toInt()
        if (data > max_data){
            max_data = data
            cnt = i
        }
    }
    println(max_data)
    print(cnt)
}