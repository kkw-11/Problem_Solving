package BruteForce;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class No2501 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        //약수 구하기
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if(n % i == 0){
                list.add(i);
            }
        }

        // 약수의 개수가 k보다 작으면 0 출력
        if(list.size() < k){
            System.out.println(0);
        }else {
            //아니면 K번째 약수 출력
            System.out.println(list.get(k-1));
        }
    }
}
