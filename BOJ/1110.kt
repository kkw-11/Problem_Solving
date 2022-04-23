import java.io.*
import java.util.*
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var num = br.readLine().toInt()

    var cur_num = num
    var each_num_sum = 0
    var right_num = 0
    var cnt = 0

    do{
        each_num_sum = (cur_num/10) + (cur_num%10)
        right_num = cur_num%10
        cur_num = right_num*10 + each_num_sum%10
        cnt += 1
    }while(cur_num != num)
    print(cnt)

}g