class Solution {
    
    var cnt = 0
    var flag = false
    
    fun solution(word: String): Int {
        var answer = 0
        var vowels = arrayOf('A','E','I','O','U')
        dfs("",vowels, word)
    
        return cnt
    }
    
    fun dfs(w:String, vowels:Array<Char>, word:String){
        if (w.length > 5){
            return
        }
        else{
            if (w.length >0){
                cnt += 1
            }
            if (w.equals(word)){
                flag = true
            }

            for(i in 0..4){
                if(flag == false)
                    dfs(w+vowels[i],vowels,word)
            }
        }
    }


}