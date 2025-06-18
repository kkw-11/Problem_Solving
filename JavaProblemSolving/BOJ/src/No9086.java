import java.util.Scanner;

public class No9086 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();

        for(int i = 0; i < count; i++) {
            String s = sc.next();
            System.out.println(s.charAt(0) + "" + s.charAt(s.length()-1));
        }
        sc.close();
    }
}
