//https://www.acmicpc.net/problem/11048
#include <stdio.h>
int candy[1001][1001];
int map[1001][1001];
int n, m;
int Bigger(int a, int b) {
    if (a > b)return a;
    else return b;
}
void Sol() {
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            int result = Bigger(Bigger(candy[i - 1][j], candy[i][j - 1]), candy[i - 1][j - 1]);
            candy[i][j] = result + map[i][j];

        }
    }
    printf("%d\n", candy[n][m]);
}

int main() {
    freopen("input.txt", "rt", stdin);

    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            scanf("%d",&map[i][j]);
        }
    }
    Sol();

    return 0;
}