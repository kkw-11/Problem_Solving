package Implement;

import java.util.Scanner;

public class No17614 {
    public static void main(String[] args) {
        int result = 0;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 1; i <= n; i++){
            int currentNum = i;
            while (true){
                int rest = currentNum % 10;
                if(rest == 3 || rest == 6 || rest == 9){
                    result += 1;
                }
                currentNum = currentNum / 10;
                if(currentNum <= 0) break;
            }

        }
        System.out.println(result);
    }
}
