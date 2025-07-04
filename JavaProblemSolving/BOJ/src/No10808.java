import java.util.Scanner;

public class No10808 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.next();

        int[] nums = new int[26];

        for (int i = 0; i < input.length(); i++) {
            int index = input.charAt(i) - 'a';
            nums[index]++;
        }

        for(int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }

        sc.close();
    }
}
