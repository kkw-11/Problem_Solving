package String;

import java.util.Scanner;

public class No1152 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine().strip();
        if (input.isBlank()) {
            System.out.println(0);
        }else {
            String[] splitInput = input.split("\\s+");

            System.out.println(splitInput.length);
        }
        scanner.close();
    }
}
