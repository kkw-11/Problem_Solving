import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    var numList = br.readLine().split(' ').map { it.toInt() }
    var max_data = -1000001
    var min_data = 1000001
    for (num in numList) {
        if (num > max_data)
            max_data = num
        if (num < min_data)
            min_data = num

    }
    print(min_data)
    print(" ")
    print(max_data)
}