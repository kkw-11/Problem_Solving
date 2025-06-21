package String;

import java.util.Scanner;

public class No2744 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        StringBuilder output = new StringBuilder();
        for(char ch : input.toCharArray()){
            if(ch >= 'A' && ch <= 'Z'){
                output.append(Character.toLowerCase(ch));
            } else if (ch >= 'a' && ch <= 'z') {
                output.append(Character.toUpperCase(ch));
            }
        }

        System.out.println(output);
    }
}
