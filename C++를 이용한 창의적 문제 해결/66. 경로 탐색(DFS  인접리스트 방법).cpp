//66. 경로 탐색(DFS : 인접리스트 방법)
#include<stdio.h>
#include<vector>
using namespace std;

int cnt, N;
int visited[21];
vector<int> map[21];

void dfs(int vertex) {
	if (vertex == N)
		++cnt;
	else {
        //vertex에 연결된 노드들에 대해 방문하지 않았으면 방문처리하고 DFS탐색 vertex가 N이 될때 까지, vertex가 N이 되면 ++cnt
    
		for (int i = 0; i < map[vertex].size(); ++i) {
			if (visited[map[vertex][i]] == 0) {
				visited[map[vertex][i]] = 1;
				dfs(map[vertex][i]);
				visited[map[vertex][i]] = 0;
			}
		}

	}

}

int main() {
	//freopen("input.txt", "rt", stdin);
	int M, a, b;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; ++i) {
		scanf("%d %d", &a, &b);
		map[a].push_back(b); //a에 연결된 간선 정보 b 연결리스트방식으로 저장
	}
	visited[1] = 1;
	dfs(1);

	printf("%d", cnt);

	return 0;
}
