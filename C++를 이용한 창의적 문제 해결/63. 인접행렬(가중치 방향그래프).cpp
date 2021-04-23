//63. 인접행렬(가중치 방향그래프)
#include <stdio.h>
#include <stdlib.h>

int main() {
	freopen("input.txt", "rt", stdin);
	int n, m, x, y, z;
	scanf("%d%d", &n, &m);
	
	//2차원 동적 배열 할당
	int** map = (int**)calloc(n+1, sizeof(int));
	for (int i = 0; i <= n; ++i) {
		map[i] = (int*)calloc(n+1, sizeof(int));	
	}

	//2차원 가중치 행렬에 대한 값을 입력
	for (int i = 0; i < m; ++i) {
		scanf("%d%d%d", &x, &y, &z);
		map[x][y] = z;
	}

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}

	return 0;
}
