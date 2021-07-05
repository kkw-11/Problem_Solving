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

    //부분집합 2^n n개의 물건에
    //2^30 -> 2^15, 2^15 ->2^16 
    for (int i = 0; i < n / 2; i++) scanf("%d", &a[i]);
    dfs(0, n / 2, 0, 1, m);
    sort(sum1, sum1 + l1);

    for (int i = n / 2; i < n; i++) scanf("%d", &a[i - (n / 2)]);
    dfs(0, n - (n / 2), 0, 2, m);
    sort(sum2, sum2 + l2);
////////
//sum1[0]

//
    for (int i = 0, j = l2 - 1; i < l1 && j >= 0; i++) {
        while (sum1[i] + sum2[j] > m) j--;
        cnt += j + 1; //j sum1[i] + sum2[j] <= m // sum1[i] + sum2[j]>m 

        //
    }
    printf("%d", cnt);
    return 0;
}
