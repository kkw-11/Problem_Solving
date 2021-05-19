//67. 최소비용(DFS : 인접행렬)
#include<stdio.h>
int N, M, minDist = 99999999;
int map[21][21], visited[21];
void dfs(int vertex, int sumDist) {
	if (vertex == N) {
		if (sumDist < minDist)
			minDist = sumDist;
	}
	else {
		for (int i = 1; i <= N; ++i) {
			if (visited[i] == 0 && map[vertex][i] != 0) {
				visited[i] = 1;
				sumDist += map[vertex][i];
				dfs(i, sumDist);
				visited[i] = 0;
				sumDist -= map[vertex][i];
			}
		}

	}

}

int main() {
	//freopen("input.txt", "rt", stdin);
	int r, c,dist;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; ++i) {
		scanf("%d %d %d", &r, &c, &dist);
		map[r][c] = dist;
	}

	dfs(1, 0);


	printf("%d", minDist);

	return 0;
}
