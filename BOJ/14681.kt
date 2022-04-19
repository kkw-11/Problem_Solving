import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
//    val (a, b) = br.readLine().split(' ').map{it.toInt()}
    val x = br.readLine().toInt()
    val y = br.readLine().toInt()

    if (x>0 && y>0)
        print(1)
    else if (x<0 &&y>0)
        print(2)
    else if (x<0 && y<0)
        print(3)
    else
        print(4)


}