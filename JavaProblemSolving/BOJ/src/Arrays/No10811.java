package Arrays;

import java.util.Scanner;

public class No10811 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = i + 1;
        }

        for(int i = 0; i < m; i++){
            int left = sc.nextInt();
            int right = sc.nextInt();
            reverse(arr, left-1, right-1);
        }

        for(int i = 0; i < n; i++){
            System.out.print(arr[i] + " ");
        }
    }

    public static void swap(int[] arr, int left, int right){
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
    }

    public static void reverse(int[] arr, int left, int right){
        while(left < right){
            swap(arr, left, right);
            left++;
            right--;
        }
    }
}
