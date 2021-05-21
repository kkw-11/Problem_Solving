//64. 경로 탐색(DFS)
#include <stdio.h>
int n, cnt = 0;
int map[20][20],visited[20];

void DFS(int vertex) {
	if (vertex == n - 1) {
		++cnt;
	}
	else {
		//i는 다음에 방문할 정점을 의미
		for (int i = 0; i < n; ++i) {
			//방문 가능한 정점(간선 연결)이고 아직 방문하지 않은 정점 조건 확인
			if (visited[i] == 0 && map[vertex][i] == 1) {
				visited[i] = 1;
				DFS(i);
				//리턴되어 돌아온 후 다시 최근 방문했던 정점에 대해 방문체크를 풀어 주어야 다시 다른 정점에서 방문가능하기 때문에 풀어줌
				visited[i] = 0;
			}
		}
	}
}

int main() {
	//freopen("input.txt", "rt", stdin);

	int m, x, y;
	scanf("%d%d", &n, &m);

	//행렬 방식으로 방향 그래프 저장
	for (int i = 0; i < m; ++i) {
		scanf("%d%d", &y, &x);
		map[y-1][x-1] = 1;
	}

	visited[0] = 1;
	DFS(0);

	printf("%d\n", cnt);

	return 0;
}


//64. 경로 탐색(DFS)
//#include<stdio.h>
//int N, M, cnt;
//int map[21][21], visited[21];
//void dfs(int v) {
//	if (v == N)
//		++cnt;
//	else {
//		for (int i = 1; i <= N; ++i) {
//			if (map[v][i] == 1 && visited[i] == 0) {
//				visited[i] = 1;
//				dfs(i);
//				visited[i] = 0;
//			}
//		}
//	}
//
//}
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int a, b, start = 1;
//	scanf("%d %d", &N, &M);
//	for (int i = 0; i < M; ++i) {
//		scanf("%d %d", &a, &b);
//		map[a][b] = 1;
//	}
//
//	visited[start] = 1;
//	dfs(start);
//	printf("%d", cnt);
//
//	return 0;
//}
