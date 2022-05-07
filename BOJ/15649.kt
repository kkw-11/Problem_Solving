import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = br.readLine().split(' ').map { it.toInt() }
    val checked = BooleanArray(n+1,{false})
    val set_nums = mutableListOf<Int>()
    choose(set_nums,n,m,checked)

}
fun choose(set_nums:MutableList<Int>,n:Int,m:Int,checked:BooleanArray){
    if (set_nums.size == m){
        for(num in set_nums){
            print("$num ")
        }
        println()
    }
    else{
        for (num in 1..n){
            if (checked[num]) continue
            checked[num] = true
            set_nums.add(num)
            choose(set_nums,n,m,checked)
            checked[num] = false
            set_nums.remove(num)
        }
    }
}

