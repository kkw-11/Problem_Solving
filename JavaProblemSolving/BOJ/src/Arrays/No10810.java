package Arrays;

import java.util.Scanner;

public class No10810 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int m = scanner.nextInt();

        int[] basket = new int[n];

        for(int i = 0; i < m; i++) {
            int firstIndex = scanner.nextInt() - 1;
            int lastIndex = scanner.nextInt() - 1;
            int ballNum = scanner.nextInt();
            for(int j = firstIndex; j <= lastIndex; j++) {
                basket[j] = ballNum;
            }
        }

        for(int i = 0; i < basket.length - 1; i++) {
            System.out.print(basket[i] + " ");
        }
        System.out.print(basket[basket.length - 1]);
    }
}
