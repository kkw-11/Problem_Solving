//70. 그래프 최단거리(BFS)

#include<stdio.h>
#include<vector>
using namespace std;


int main() {
	freopen("input.txt", "rt", stdin);
	int Q[10] = {0}, visited[10] = { false, };
	int front=-1, rear=-1, x, a, b,firstX = 1;
	vector<int> map[10];

	for (int i = 0; i < 6; ++i) {
		scanf("%d %d", &a, &b);
		map[a].push_back(b);
		map[b].push_back(a);
	}

	Q[++rear] = firstX;
	visited[firstX] = true;

	while (front < rear) {
		x = Q[++front];
		printf("%d ", x);
		for (int i = 0; i < map[x].size(); ++i) {
			if (visited[map[x][i]] == false) {
				Q[++rear] = map[x][i];
				visited[map[x][i]] = true;
			}
		}
	}

	return 0;
}


// #include<stdio.h>
// #include<vector>
// #include<algorithm>
// using namespace std;
// int Q[100], front=-1, rear=-1, visited[10];
// vector<int> map[10];

// int main(){
// 	//freopen("input.txt", "rt", stdin);
// 	int i, a, b, x, firstX= 1;
//     for(i=1; i<=6; i++){
// 		scanf("%d %d", &a, &b);
// 		map[a].push_back(b);
// 		map[b].push_back(a);
// 	}

//     //Queue에는 rear부터 넣어준다.    
// 	Q[++rear] = firstX;
// 	visited[firstX] = 1;

// 	while(front<rear){
// 		x=Q[++front];
// 		printf("%d ", x);
//         //x에 연결된 부분을 저장해두었던 인접리스트로 표현해 2차원 vector에 각 노드에 연결된 사이즈 만큼 for문으로 확인
// 		for(i=0; i<map[x].size(); ++i){
//             printf("%d ",map[x][i]);

//             //queue에서 빼준(queue에는 가장 먼저들어 간 순서대로 빠진다.) 노드에 연결된 부분을 순차적으로 방문확인하고
//             //방문 하지 않았으면 방문처리하고 Queue에 넣어준다.
// 			if(visited[map[x][i]] == 0){
// 				visited[map[x][i]] = 1;
// 				Q[++rear] = map[x][i];
// 			}
// 		}
//         printf("\n");
// 	}
// 	return 0;
// }

// #include<stdio.h>
// #include<vector>
// #include<algorithm>
// using namespace std;
// //front와 rear를 활용해 배열 Q를 자료구조 queue를 간단하게 구현
// int Q[100], front = -1, rear = -1, ch[10];
// vector<int> map[10];//map이라는 벡터가 10개 생성

// void bfs(int start) {
//     int x;
//     Q[++rear] = start;
//     ch[0] = start;
//     while (front < rear) {
//         x = Q[++front];
//         printf("%d", x);
//         for (int i = 0; i < map[x].size(); ++i) {
//             if (ch[map[x][i]] == 0) {
//                 ch[map[x][i]] = 1;
//                 Q[++rear] = map[x][i];
//             }
//         }
//     }
// }

// int main() {
//     freopen("input.txt", "rt", stdin);
//     int a, b;
//     for (int i = 0; i < 6; ++i) {
//         // 간선정보 입력 받고
//         scanf("%d %d", &a, &b);
//         //무방향 그래프 연결리스트 방식으로 생성
//         map[a].push_back(b);
//         map[b].push_back(a);
//     }
//     bfs(1);
//     return 0;
// }


// #include<stdio.h>
// #include<vector>
// #include<algorithm>
// using namespace std;
// int Q[100], front = -1, rear = -1, ch[10];
// vector<int> map[10];//map이라는 벡터가 10개 생성
// void bfs(int start){
//   Q[++rear] = start;
//     ch[0] = start;
//     while(front<rear){
//         int x = Q[++front];
//         printf("%d",x);
//         for(int i = 0;i<map[x].size();++i){
//             if(ch[map[x][i]]==0){
//                 ch[map[x][i]] = 1;
//                 Q[++rear] = map[x][i];
//             }
//         }
//     }


// }
// int main(){
//     int a,b,x;
//     for(int i = 0;i<6;++i){
//         scanf("%d %d",&a,&b);
//         map[a].push_back(b);
//         map[b].push_back(a);
//     }


//     bfs(1);
//       return 0;
// }