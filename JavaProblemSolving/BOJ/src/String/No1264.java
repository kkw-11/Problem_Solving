package String;

import java.util.Scanner;

public class No1264 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String vowels = "aeiouAEIOU";

        while (true) {
            String s = scanner.nextLine();
            if(s.equals("#")) {
                break;
            }
            int count = 0;

            for(char c : s.toCharArray()) {
                if(vowels.indexOf(c) == -1) {
                    count++;
                }
            }
            System.out.println(count);
        }
        scanner.close();
    }
}
