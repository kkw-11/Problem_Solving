package Arrays;

import java.util.Scanner;

public class No10831 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = i + 1;
        }

        for(int i = 0 ; i < m ; i++){
            int firstIndex = sc.nextInt();
            int secondIndex = sc.nextInt();
            int tmp = 0;
            tmp = arr[secondIndex-1];
            arr[secondIndex-1] = arr[firstIndex-1];
            arr[firstIndex-1] = tmp;
        }

        for(int a : arr){
            System.out.print(a + " ");
        }
    }
}
