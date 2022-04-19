import java.util.Scanner
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val score = br.readLine().toInt()

    if (score>=90 && score<=100){
        println("A")
    }
    else if(score>=80 && score<90){
        println("B")
    }
    else if(score>=70 && score<80){
        println("C")
    }
    else if(score>=60 && score<79){
        println("D")
    }
    else
        print("F")

}