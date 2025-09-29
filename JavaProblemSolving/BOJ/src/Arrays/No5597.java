package Arrays;


import java.util.Scanner;

public class No5597 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean[] students = new boolean[30];

        for (int i = 0; i < 28; i++) {
            int studentNum = sc.nextInt();
            students[studentNum-1] = true;
        }
        for (int i = 0; i < 30; i++) {
            if (!students[i]) {
                System.out.println(i + 1);
            }
        }
    }
}
