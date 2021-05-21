//68. 최소비용(DFS : 가중치 방향그래프 인접리스트)
//68. 최소비용(DFS : 가중치 방향그래프 인접리스트)
#include<stdio.h>
#include<queue>
#include<algorithm>
using namespace std;
int N, M, minDist = 9999999;
int visited[30];
vector<pair<int, int> > map[30];
void dfs(int vertex, int sum) {
	if (vertex == N) {
		if (sum < minDist) minDist = sum;
	}
	else {
		for (int i = 0; i < map[vertex].size(); ++i) {
			if (visited[map[vertex][i].first] == 0) {
				visited[map[vertex][i].first] = 1;
				dfs(map[vertex][i].first, sum + map[vertex][i].second);
				visited[map[vertex][i].first] = 0;
			}
		}
	}
}

int main() {
	//freopen("input.txt", "rt", stdin);
	int r, c, dist;
	scanf("%d %d", &N, &M);

	for (int i = 0; i < M; ++i) {
		scanf("%d %d %d", &r, &c, &dist);
		map[r].push_back(make_pair(c,dist));//push_back함수를 통해 make_pair함수를 통해 pair형으로 만들어진 자료를 넣는다.
	}

	dfs(1, 0);

	printf("%d", minDist);


	return 0;
}

