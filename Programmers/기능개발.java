import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] result = new int[progresses.length];
        int cnt = 0;

        List<Integer> deploymentDay = new ArrayList<>();

        for (int i = 0; i < progresses.length; ++i) {
            deploymentDay.add((int) (Math.ceil((double) (100 - progresses[i]) / speeds[i])));
        }
        Stack<Integer> deploymentLeadDayStack = new Stack<>();
        Integer leftMaxNum = 0;

        for (int i = 0; i < progresses.length; ++i) {
            if (deploymentLeadDayStack.isEmpty()) {
                deploymentLeadDayStack.push(deploymentDay.get(i));
                leftMaxNum = deploymentDay.get(i);
            } else {
                if (deploymentDay.get(i) <= leftMaxNum) {
                    deploymentLeadDayStack.push(deploymentDay.get(i));
                } else {
                    result[cnt++] = deploymentLeadDayStack.size();
                    deploymentLeadDayStack.removeAllElements();
                    leftMaxNum = deploymentDay.get(i);
                    deploymentLeadDayStack.push(deploymentDay.get(i));

                }
            }

        }
        if (!deploymentLeadDayStack.isEmpty()) {
            result[cnt++] = deploymentLeadDayStack.size();
        }

        int[] answer = new int[cnt];
        System.arraycopy(result, 0, answer, 0, cnt);

        return answer;
    }
}
