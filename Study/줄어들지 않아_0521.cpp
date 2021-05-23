//https://www.acmicpc.net/problem/2688
#include <stdio.h>
typedef long long ll;
ll dp[65][11]; //dp[i][j] / i자리에j가 들어갈 수 있는 수의 개수 //dp[3][2] = 11
int T, n;
//dp[3][2]
//dp[3][2] = dp[2][2] + dp[3][1] 
//002 012 022 112 122 222
//02 12 22
//001 011 111 dp[3][1]
// dp[i][j] = dp[i][j-1] + dp[i-1][j] 
ll neverdown(int maxDigit) {

    //점화식 구현을 위해 초기항 셋팅
    for (int digit = 1; digit <= maxDigit; digit++)
        dp[digit][0] = 1;
    for (int num = 0; num < 10; num++)
        dp[1][num] = 1;


    for (int digit = 1; digit <= maxDigit; digit++) {
        for (int num = 1; num <= 9; num++) {
            dp[digit][num] = dp[digit - 1][num] + dp[digit][num - 1];
        }
    }
    
    
    ll res = 0;
    for (int num = 0; num <=9; num++)
        res += dp[maxDigit][num];
    return res;
}
 
int main() {
    int T,n;
    scanf("%d",&T);

    while (T--) {
        scanf("%d",&n);
        printf("%d\n",neverdown(n));
    }

}



// #include <stdio.h>

// bool check(int n, int digit){

//     int rightNum, leftNum;
//     bool incresingNum = true;

//     for (int i = 0; i < digit-1; ++i){
//         rightNum = n % 10; //3 2
//             n /= 10;           //12, 1
//             leftNum = n % 10;  //2 1
//             if (leftNum > rightNum)
//             {
//                 incresingNum = false;
//                 break;
//             }
//     }
            
//     return incresingNum;
// }

// int main(){

//     if (check(321, 3))
//         printf("Yes incresing number");
//     else
//         printf("No incresing number ")

//     return 0;
// }