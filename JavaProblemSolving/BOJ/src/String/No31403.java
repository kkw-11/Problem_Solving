package String;

import java.util.Scanner;

public class No31403 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.println(a + b - c);

        String ab = a + "" + b;

        int numericValue = Character.getNumericValue(ab.charAt(0));
        System.out.println(numericValue * 10 + Character.getNumericValue(ab.charAt(1)) - c);
    }
}
