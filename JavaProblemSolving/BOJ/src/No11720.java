import java.util.Scanner;

public class No11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String inputLength = sc.next();

        String inputNum = sc.next();

        int sum = 0;

        for (int i = 0; i < inputNum.length(); i++) {
            sum += inputNum.charAt(i) - '0';
        }

        System.out.println(sum);
    }
}
