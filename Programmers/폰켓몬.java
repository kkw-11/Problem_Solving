import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;

        int halfNumsLen = nums.length/2;

        Set<Integer> ponKetMonSet = new HashSet<>();
        for (Integer ponKetMonNum : nums) {
            ponKetMonSet.add(ponKetMonNum);
        }

        if (ponKetMonSet.size() > halfNumsLen) {
            answer = halfNumsLen;
        } else {
            answer = ponKetMonSet.size();
        }

        return answer;
    }
}
