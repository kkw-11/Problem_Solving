// https://www.acmicpc.net/problem/1450
#include <stdio.h>
int sum, i, j, c, n, cnt;
int num[30];
void go(int c, int i, int j, int sum) {
    if (i == n) return;

    if (c == sum) {
        ++cnt;
        ++j;
        sum = 0;
        if (j == n) {
            ++i;
            if (i == n) return;
            j = i + 1;
           sum = sum + num[i];
        }
    }
    else if (c < sum) {
        sum -= num[j];
        ++j;
        if (j == n) {
            sum = 0;
            ++i;
            if (i == n) return;
            j = i + 1;
            sum = sum + num[i];
        }
    }

    go(c, i, j, sum + num[j]);

}


int main() {
    freopen("input.txt", "rt", stdin);
    scanf("%d%d", &n, &c);
    for (int k = 0; k < n; ++k) {
        scanf("%d", &num[k]);
    }

    j = i + 1;
    sum += num[i];
    go(c, i, j, sum);

    printf("%d", cnt);

    return 0;
}

