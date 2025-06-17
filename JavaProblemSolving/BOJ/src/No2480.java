import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class No2480 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        Integer[] arr = new Integer[3];
        for(int i = 0;i < 3; ++i){
            arr[i] = sc.nextInt();
        }
        int answer = 0;
        //3개가 같은 경우
        if(arr[0].equals(arr[1]) && arr[0].equals(arr[2])){
            answer = 10000 + arr[0]*1000;
        //3개가 모두 다른 경우
        }
        else if (!arr[0].equals(arr[1]) && !arr[1].equals(arr[2]) && !arr[0].equals(arr[2])) {
            Arrays.sort(arr, Collections.reverseOrder());
            answer = arr[0]*100;
        //그외 => 2개만 같은 경우
        }else {
            Arrays.sort(arr, Collections.reverseOrder());
            if(arr[0].equals(arr[1])){
                answer = 1000 + arr[0]*100;
            }else{
                answer = 1000 + arr[1]*100;
            }
        }
        System.out.println(answer);
    }
}
