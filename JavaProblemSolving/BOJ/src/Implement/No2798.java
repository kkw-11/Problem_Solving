package Implement;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class No2798 {
    public static void main(String[] args) {
        //N장중 3장을 골라 M을 넘지 않으면서 M과 최대한 가까운 3장의 합

        // 입력
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] nums = new int[n];
        for(int i = 0;i < n;++i){
            nums[i] = sc.nextInt();
        }

        List<Integer> sums = new ArrayList<>();

        // 반복문으로 각 인덱스마다 두 장 카드 더해서 리스트에 보관,
        for(int i = 0;i < n; ++i){
            for(int j = i+1;j < n; ++j){
                for(int k = j+1;k < n; ++k){
                    int sum = nums[i] + nums[j] + nums[k];
                    sums.add(sum);
                }
            }
        }

        int diffMin = Integer.MAX_VALUE;
        int diff = Integer.MAX_VALUE;
        int result = 0;
        // 보관한 값 M이랑 비교 가장 가까운 값 찾기, 비교값은 차이로 반복 비교
        for (Integer sum : sums) {
            //m이랑 비교최소
            if(m >= sum){
                diff = m - sum;
            }

            if(diff < diffMin){
                diffMin = diff;
                result = sum;
            }
        }
        System.out.println(result);
    }
}
