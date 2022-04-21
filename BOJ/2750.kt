import java.io.*
import java.util.*
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var n = br.readLine().toInt()
    var nums = mutableListOf<Int>()
    for (i in 0..n-1){
        nums.add(br.readLine().toInt())
    }
    nums.sort()

    for(num in nums){
        println(num)
    }
}