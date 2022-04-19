import java.io.*
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var a = br.readLine().toInt()
    var b = br.readLine().toInt()
    var c = br.readLine().toInt()
    var total = a*b*c
    val intArray = IntArray(10,{0})

    while(total != 0){
        intArray[total%10] += 1
        total /= 10
    }

    for (data in intArray){
        println(data)
    }

}