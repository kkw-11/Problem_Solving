import java.util.Stack;
class Solution
{
    public int solution(String s)
    {
        int answer = -1;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        Stack<Character> stack = new Stack<Character>();
        
        for(int i = 0; i < s.length(); ++i){
            Character ch = s.charAt(i);
            if(!stack.empty()){
                if(stack.peek() != ch){
                    stack.push(ch);
                }
                else{
                    stack.pop();
                }
            }
            else{
                stack.push(ch);
            }
        }
        
        if(stack.empty()){
            return 1;
        }
        else{
            return 0;
        }

    }
}