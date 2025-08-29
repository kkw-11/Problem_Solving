package Implement;

import java.util.Scanner;

public class No19532 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        //입력 받는다.
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int e = sc.nextInt();
        int f = sc.nextInt();

        //2차방정식의 해인, x,y를 주어진 a,b,c,d,e,f로 표현하고 출력한다.
        double k = (double) d/a;
        int y = (int)((c*k-f)/(b*k- e));
        int x = (d-b*y)/a;

        System.out.println(x + " " + y);
    }
}
