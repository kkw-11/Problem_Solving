import java.util.Scanner;

public class No27866 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();

        int inputInt = scanner.nextInt();

        System.out.println(inputString.charAt(inputInt-1));
        scanner.close();

    }
}
