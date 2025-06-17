import java.util.Scanner;

public class No10807 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //입력
        int answer = 0;
        int n = sc.nextInt();
        int[] nums = new int[n];

        for(int i = 0;i < n; ++i){
            nums[i] = sc.nextInt();
        }

        int v = sc.nextInt();
        //비교 출력 로직
        for(int i = 0;i < n; ++i){
            if(nums[i] == v)
                answer++;
        }

        System.out.println(answer);
    }

}
