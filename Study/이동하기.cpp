//https://www.acmicpc.net/problem/11048
#include <stdio.h>
int candy[1001][1001];
int map[1001][1001];
int n, m;
int Bigger(int a, int b) {
    if (a > b)return a;
    else return b;
}

//아래로 이동을 i-1
//우측 으로 이동하는 것을 j-1
////i-1,j-1
//(1,1)
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




///////////////////////////////////////////////////////////////////////////////////////
//스터디원 파이썬 공유 코드
// # 2) 가능 방법
// # bottom-up이, 이전 칸에서 오는 방식이었다면
// # 3번째 방법은, 현재 칸에서, 다음칸으로 가는 방식을 취한다
// n, m = map(int, input().split())
// a = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
// d = [[0]*(m+1) for _ in range(n+1)]
// d[1][1] = a[1][1]
// # 참고 : 2번째 방법과 3번째 방법에서 d[i][j]에 들어있는 값은 동일하다
// # 그저, 점화식을 채우는 방식만 바뀔 뿐인 것이다
// for i in range(1, n+1):
//     for j in range(1, m+1):
//         # 가로 
//         if j+1 <= m and d[i][j+1] < d[i][j] + a[i][j+1]:
//             d[i][j+1] = d[i][j] + a[i][j+1]
//         # 세로 
//         if i+1 <= n and d[i+1][j] < d[i][j] + a[i+1][j]:
//             d[i+1][j] = d[i][j] + a[i+1][j]
//         # 대각선 
//         if i+1 <= n and j+1 <= m and d[i+1][j+1] < d[i][j] + a[i+1][j+1]:
//             d[i+1][j+1] = d[i][j] + a[i+1][j+1]
// print(d[n][m])


// # 3) 3번째 방법
// # 여기서는, 그저 대각선을 가는 방법이 사실 의미가 없다는 것이다
// # 왜냐하면, a[i][j]는 모두 0보다 크거나 같으며
// # 최댓값을 구하는 과정이기 때문에
// # 사실, 대각선으로 가는 것보다는
// # 오른쪽 + 아래 // 아래 + 오른쪽 --> 대각선으로 가는 과정보다 더 크거나 같기 때문이다
// # ( 중요 ) a[i][j]가 0보다 크거나 같다는 조건이 있기 때문에 가능한 것이다
// n, m = map(int, input().split())
// a = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
// d = [[0]*(m+1) for _ in range(n+1)]
// for i in range(1, n+1):
//     for j in range(1, m+1):
//         d[i][j] = max(d[i-1][j], d[i][j-1])+a[i][j]
// print(d[n][m])
// d = [[-1]*(m+1) for _ in range(n+1)]


// def go(i, j):
//     # bottom up과 달리, 범위를 정해주는 과정
//     if i < 1 or j < 1:  # i,j 가 1보다 작으면, 불가능한 경우 --> 0을 return
//         return 0
//     if d[i][j] >= 0:  # memoization --> top-down 과정에서 가장 중요한 것
//         return d[i][j]
//     d[i][j] = max(go(i-1, j), go(i, j-1))+a[i][j]
//     return d[i][j]

// # dp : recursive(재귀) + memoization(저장)


// print(go(n, m))


// 방법 4
// Top-Down -----------------------------------------------
// # d[i][j]가 '시작점'에서 (i,j)로 가는 것을 의미했다면
// # 여기서는 (i,j) 에서 '도착점'까지 가는 것으로 정의하려고 한다
// # 그 말은 즉슨 (1,1)로 갈수록, 더 큰 문제에 해당하게 되는 것이다
// sys.setrecursionlimit(1000000)
// n, m = map(int, input().split())
// a = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
// d = [[-1]*(m+1) for _ in range(n+1)]


// def go(i, j):  # go(i,j) : i,j 에서 끝점까의 최대 캔디 개수
//     if i > n or j > m:
//         return 0
//     if d[i][j] >= 0:
//         return d[i][j]
//     d[i][...
