//65. 미로탐색(DFS)

#include <stdio.h>
int map[7][7], visited[7][7];
int dx[] = { 1,0,-1,0 };
int dy[] = { 0,1,0,-1 };
int cnt;

void go(int y, int x) {
	if (y == 6 && x == 6) {
		++cnt;
	}
	else {
		for (int i = 0; i < 4; ++i) {
			// xx, yy는 다음에 갈 곳, x,y는 현재 위치
			int xx = x + dx[i];
			int yy = y + dy[i];

			if (xx >= 0 && xx < 7 && yy >= 0 && yy < 7 && map[yy][xx] == 0 && visited[yy][xx] == 0) { 
				visited[yy][xx] = 1;
				go(yy, xx);
				//직전에 방문 한곳 다시 미방문 처리
				visited[yy][xx] = 0;
			}
		}
	}
}

int main() {
	freopen("input.txt", "rt", stdin);

	for (int i = 0; i < 7; ++i) {
		for (int j = 0; j < 7; ++j) {
			scanf("%d", &map[i][j]);
		}
	}

	visited[0][0] = 1;
	go(0, 0);

	printf("%d", cnt);
	return 0;
}
