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
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx >= 0 && nx < 7 && ny >= 0 && ny < 7 && map[ny][nx] == 0 && visited[ny][nx] == 0) { 
				visited[ny][nx] = 1;
				go(ny, nx);
				//직전에 방문 한곳 다시 미방문 처리
				visited[ny][nx] = 0;
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
