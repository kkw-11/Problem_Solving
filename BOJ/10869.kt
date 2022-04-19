import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b) = br.readLine().split(' ').map{it.toInt()}

    println(a+b)
    println(a-b)
    println(a*b)
    println(a/b)
    println(a%b)


}