package String;

import java.util.Arrays;
import java.util.Scanner;

public class No10809 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String inputString = sc.next();

        int[] alphabetArr = new int[26];
        Arrays.fill(alphabetArr, -1);

        for(int stringIndex = 0; stringIndex < inputString.length(); stringIndex++) {
            //문자열 문자의 알파벳 위치 구하기
            int alphabetSeq = inputString.charAt(stringIndex) - 'a';
            //첫 등장 체크, 첫 등장이면 위치값 저장
            if(alphabetArr[alphabetSeq] == -1) {
                alphabetArr[alphabetSeq] = stringIndex;
            }
        }

        //출력
        for(int result : alphabetArr) {
            System.out.print(result + " ");
        }

        sc.close();
    }
}
