import java.util.Scanner;

public class No10871 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();

        int[] arrays = new int[n];

        for(int i = 0;i < n; ++i){
            arrays[i] = sc.nextInt();
        }

        for(int i = 0;i < n; ++i){
            if(arrays[i] < x){
                System.out.print(arrays[i] + " ");
            }

        }

    }
}
