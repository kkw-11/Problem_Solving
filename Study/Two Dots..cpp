//https://www.acmicpc.net/problem/16929

#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;

char map[50][50];
int n, m;
//상하좌우
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };
bool visited[50][50];
int result = 0;
pair<int, int> start;

void dfs(int x, int y, char ch, int depth) {
	for (int i = 0; i < 4; ++i) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
			if (map[nx][ny] == ch) {
				if (depth >= 3 && nx== start.first && ny == start.second) {
				//	printf("%d, %d, %c\n%d", x,y, map[nx][ny],depth);
					result = 1;
					return;
				}

				if (visited[nx][ny] == true) continue;
				visited[nx][ny] = true;

				dfs(nx, ny, ch, depth + 1);

			}
		}

	}
}
 
int main() {
	freopen("input.txt", "rt", stdin);
	//입력
	scanf("%d %d", &n, &m);
	getchar();
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			scanf("%c", &map[i][j]);
			//printf("%c", map[i][j]);
		}
		//printf("\n");
		getchar();
	}

	//알고리즘
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			start = { i,j };
			visited[i][j] = true;
			dfs(i, j, map[i][j], 1);

			for (int t = 0; t < n; ++t) {
				fill(visited[t], visited[t] + m, false);
			}

			if (result == 1) {
				printf("Yes");
				return 0;
			}

		}
	}
	printf("No");

	return 0;
}


///////////////////////////////////////////////////////////////////////////////////////
// 아래코드는 리패토링전 스터디 코드

// #include <iostream>
// #include <cstring>
// using namespace std;
// char a[55][55];
// bool check[55][55];
// int dist[55][55];
// int n, m;
// int dx[] = {0,0,1,-1};
// int dy[] = {1,-1,0,0};
// bool go(int x, int y, int cnt, char color) {
//     if (check[x][y]) {
//         if (cnt-dist[x][y] >= 4) {
//             return true;
//         } else {
//             return false;
//         }
//     }
//     check[x][y] = true;
//     dist[x][y] = cnt;
//     for (int k=0; k<4; k++) {
//         int nx = x+dx[k];
//         int ny = y+dy[k];
//         if (0 <= nx && nx < n && 0 <= ny && ny < m) {
//             if (a[nx][ny] == color) {
//                 if (go(nx, ny, cnt+1, color)) {
//                     return true;
//                 }
//             }
//         }
//     }
//     return false;
// }
// int main() {
//     cin >> n >> m;
//     for (int i=0; i<n; i++) {
//         cin >> a[i];
//     }
//     for (int i=0; i<n; i++) {
//         for (int j=0; j<m; j++) {
//             if (check[i][j]) continue;
//             memset(dist,0,sizeof(dist));
//             bool ok = go(i, j, 1, a[i][j]);
//             if (ok) {
//                 cout << "Yes" << '\n';
//                 return 0;
//             }
//         }
//     }
//     cout << "No" << '\n';
//     return 0;
// }