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