package Sort;

import java.util.*;

public class No2750 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < n; i++){
            int num = sc.nextInt();
            list.add(num);
        }
        list.sort(Comparator.naturalOrder());

        for(int num : list){
            System.out.println(num);
        }
    }
}
