//https://www.acmicpc.net/problem/1450
#include<cstdio>
#include<algorithm>
using namespace std;

#define mxl 30
#define mxn 30
int sum1[mxl], sum2[mxl], l1, l2, a[mxn];

void dfs(int start, int end, int sum, int flag, int m) {
    if (sum > m) return;
    if (start == end) {
        if (flag == 1) sum1[l1++] = sum;
        else sum2[l2++] = sum;
        return;
    }
    dfs(start + 1, end, sum, flag, m);
    dfs(start + 1, end, sum + a[start], flag, m);
}
int main() {
    freopen("input.txt", "rt", stdin);
    int n, m, cnt = 0;
    scanf("%d%d", &n, &m);

    for (int i = 0; i < n / 2; i++) scanf("%d", &a[i]);
    dfs(0, n / 2, 0, 1, m);
    sort(sum1, sum1 + l1);

    for (int i = n / 2; i < n; i++) scanf("%d", &a[i - (n / 2)]);
    dfs(0, n - (n / 2), 0, 2, m);
    sort(sum2, sum2 + l2);

    for (int i = 0, j = l2 - 1; i < l1 && j >= 0; i++) {
        while (sum1[i] + sum2[j] > m) j--;
        cnt += j + 1;
    }
    printf("%d", cnt);
    return 0;
}

// // https://www.acmicpc.net/problem/1450

// //pseudo code
// //냅색 알고리즘 인프런 강좌 학습하고 보기
// #include <stdio.h>
// int sum, i, j, c, n, cnt;
// int num[30];

// //10 3
// //2 1 1 3 1 1 1 4 5 
// //i값이 N이 되었을 때 
// //3 -> --2

// void go(int c, int i, int j, int sum) {
//     if (i == n) return;

//     if (c == sum) {
//         ++cnt;
//         ++j;
//         sum = 0;
//         if (j == n) {
//             ++i;
//             if (i == n) return;
//             j = i + 1;
//            sum = sum + num[i];
//         }
//     }
//     else if (c < sum) {
//         sum -= num[j];
//         ++j;
//         if (j == n) {
//             sum = 0;
//             ++i;
//             if (i == n) return;
//             j = i + 1;
//             sum = sum + num[i];
//         }
//     }

//     go(--c, i, j, sum + num[j]);

// }


// int main() {
//     freopen("input.txt", "rt", stdin);
//     scanf("%d%d", &n, &c);
//     for (int k = 0; k < n; ++k) {
//         scanf("%d", &num[k]);
//     }

//     j = i + 1;
//     sum += num[i];
//     go(c, i, j, sum);

//     printf("%d", cnt);

//     return 0;
// }

