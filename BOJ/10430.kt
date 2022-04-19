import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b, c) = br.readLine().split(' ').map{it.toInt()}
//    val x = br.readLine().toInt()

    println((a+b)%c)
    println(((a%c)+(b%c))%c)
    println((a*b)%c)
    println((a%c)*(b%c)%c)

}