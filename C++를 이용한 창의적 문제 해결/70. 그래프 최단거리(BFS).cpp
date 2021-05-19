//70. 그래프 최단거리(BFS)

#include<stdio.h>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	//freopen("input.txt", "rt", stdin);
	int N, M, a, b, x, start = 1;
	int distance[10] = { 0, }, visited[10] = {0,};
	vector<int> map[10];
	queue<int> q;
	scanf("%d %d", &N, &M);

	//입력 정보로 부터 그래프를 인접리스트방식으로 저장
	for (int i = 0; i < M; ++i) {
		scanf("%d %d", &a, &b);
		map[a].push_back(b);
	}

    //큐에는 처음에 탐색할 노드의 정보를 먼저 넣어주고 방문처리를 해준다.
	q.push(start);
	visited[start] = 1;
    /*
    큐에 데이터가 빌 때 까지 BFS로 노드들을 탐색하며 최소 간선수를 구한다.
    큐에서 데이터(노드번호)를 빼면서 다음에 탐색할 노드정보를 기록하기 위해 빠진 노드와 연결된 노드들을 큐에 넣어준다.  
    이때 방문했던 노드를 또 방문하지 않기 위해 큐에 넣으면서 방문 처리를 해준다.
    큐에 넣어주면서 방문할 노드까지의 최소간선수를 구하는 방법은 부모노드까지의 간선수에서 +1을 해주면 된다.
    */
    
	while (!(q.empty())) {
		x = q.front();
		q.pop();
		for (int j = 0; j < map[x].size(); ++j) {
			if (visited[map[x][j]] == 0) {
				q.push(map[x][j]); //x와 연결된 정점들을 큐에 푸시해준다. 큐는 다음에 탐색해야 할 노드들을 알기 위해 적합한 FIFO형식의 자료구조
				visited[map[x][j]] = 1;
				distance[map[x][j]] = distance[x] + 1; //x와 연결된 노드들을 탐색하고 있으므로 x와 연결된 노드까지 최소 거리는 x까지의 거리에서 +1을 하면된다. 
			}

		}
	}

	for (int i = 2; i <= N; ++i) {
		printf("%d : %d\n", i, distance[i]);
	}


	return 0;
}
