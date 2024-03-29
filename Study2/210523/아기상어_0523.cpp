// //https://www.acmicpc.net/problem/16236
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int map[20][20];
int visited[20][20];
int dr[] = { -1,1,0,0 };
int dc[] = { 0,0,-1,1 };
int n;
int Sharksize = 2;
int ateCnt;

struct Shark {
	int row, column;
};
vector<pair<int, pair<int, int>>> eatFish;

void BFS(Shark sharkStart) {
	
	queue<Shark> q;
	q.push(sharkStart);

	while (!q.empty()) {
		Shark cur;
		cur.row = q.front().row;
		cur.column = q.front().column;
		q.pop();

		for (int i = 0; i < 4; ++i) {
			Shark next;
			next.row = cur.row + dr[i];
			next.column = cur.column + dc[i];

			if (next.row < 0 || next.row >= n || next.column < 0 || next.column >= n)continue;
			if (visited[next.row][next.column]) continue;
			if (map[next.row][next.column] == 0 || map[next.row][next.column] <= Sharksize) {
				visited[next.row][next.column] = visited[cur.row][cur.column] + 1;

				q.push(next);

				if (map[next.row][next.column] > 0 && map[next.row][next.column] < Sharksize) {
					eatFish.push_back({ visited[next.row][next.column], { next.row, next.column} });
				}

			}

		}
	}
}

int main() {
//	freopen("input.txt", "rt", stdin);
	Shark sharkStart;

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			scanf("%d", &map[i][j]);
			if (map[i][j] == 9) {
				map[i][j] = 0;
				sharkStart.row = i;
				sharkStart.column = j;
			}
		}
	}

	int flag = true;
	int result = 0;

	while (flag) {
		flag = false;

		BFS(sharkStart);

		if (eatFish.size() == 0) break;
		else {
			flag = true;
			sort(eatFish.begin(), eatFish.end());
			result += eatFish[0].first;
			sharkStart.row = eatFish[0].second.first;
			sharkStart.column = eatFish[0].second.second;
			map[eatFish[0].second.first][eatFish[0].second.second] = 0;
			++ateCnt;
			if (ateCnt == Sharksize) {
				++Sharksize;
				ateCnt = 0;
			}
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					visited[i][j] = 0;
				}
			}

			eatFish.clear();
			
		}
	}

	printf("%d", result);

	return 0;
}


///////////////////////////////////////////////////////////////////////////////////////
// 리팩토링 전 학습내용 정리 코드

// #include<iostream>
// #include<queue>
// #include<vector>
// #include<stdio.h>
// #include<stdlib.h>
// #include<string.h>
// #include<math.h>
// #include<algorithm>
// using namespace std;

// #define MAX 21
// #define MIN 987654321

// int N;
// int result = 0;
// int eat_count = 0;
// int baby_size = 2;
// int eat_distance;
// int arr[MAX][MAX];
// int visit[MAX][MAX];
// int Baby_x, Baby_y;
// vector <pair <pair<int, int>, int>> Eat; //< <거리,x> y>

// int dx[4] = { 0, 0, -1, 1 };
// int dy[4] = { -1, 1, 0, 0 };

// void BFS(int init_x, int init_y) {
// 	eat_distance = MIN;
// 	Eat.clear();
// 	memset(visit, 0, sizeof(visit));

// 	queue<pair<int, int> > que; 

// 	que.push(make_pair(init_x, init_y));

// 	while (!que.empty()) {
// 		int x = que.front().first; 
// 		int y = que.front().second;
// 		que.pop();

// 		for (int i = 0; i < 4; i++) {
// 			int nx = x + dx[i]; 
// 			int ny = y + dy[i];
			
// 			if (0 > nx || N <= nx || 0 > ny || N <= ny) continue;

// 			if (visit[nx][ny] == 0 && baby_size >= arr[nx][ny]) { // 자기보다 큰 물고기 자리 못감
// 				visit[nx][ny] = visit[x][y] + 1;

// 				if (arr[nx][ny] > 0 && arr[nx][ny] < baby_size) {// 자기보다 작은 물고기 꿀꺽
					
						// Eat.push_back(make_pair(make_pair(eat_distance, nx), ny));
// 				}

// 				que.push(make_pair(nx, ny));
// 			}
// 		}
// 	}

// }

// void init() {
// 	ios::sync_with_stdio(false);
// 	cin.tie(0); cout.tie(0);
// }

// int main() {
// 	init();
// 	cin >> N;

// 	for (int i = 0; i < N; i++) {
// 		for (int j = 0; j < N; j++) {
// 			cin >> arr[i][j];

// 			if (arr[i][j] == 9) { //아기 상어
// 				arr[i][j] = 0;
// 				Baby_x = i; 
// 				Baby_y = j;
// 			}
// 		}
// 	}
	
// 	while (1) {
// 		BFS(Baby_x, Baby_y);

// 		if (Eat.empty()) break;
// 		else {
// 			sort(Eat.begin(), Eat.end());//
// 			eat_count++;
// 			result += Eat[0].first.first;//(distance,x,y) //< <거리,x> y>
// 			arr[Eat[0].first.second][Eat[0].second] = 0;
// 			//물고기 먹은후 상어 위치 갱신
// 			Baby_x = Eat[0].first.second; 
// 			Baby_y = Eat[0].second;
			
// 			if (baby_size == eat_count) {
// 				baby_size++; 
// 				eat_count = 0;
// 			}
// 		}
// 	}

// 	cout << result;
// 	return 0;
// }

// //https://www.acmicpc.net/problem/16236
// //변수명 수정
// #include <iostream>
// #include <queue>
// #include <algorithm>
// #include <cstring>
// #include <vector>
// using namespace std;
// int map[21][21];
// int visited[21][21]; //방문처리 및 현재 위치까지 이동 가능한 최소거리
// int dr[4] = { -1,0,0,1 };
// int dc[4] = { 0,-1,1,0 };
// int sharkSize = 2;
// int n;
// int sharkY;
// int sharkX;
// int ateCnt;
// int answerTime;
// bool ateFlag = false;

// void createMap() {
// 	scanf("%d", &n);
// 	for (int i = 0; i < n; i++) {
// 		for (int j = 0; j < n; j++) {
// 			std::cin >> map[i][j];
// 			if (map[i][j] == 9) {
// 				sharkY = i;
// 				sharkX = j;
// 				map[i][j] = 0;
// 			}
// 		}
// 	}
// }

// void bfs() {
// 	//이동하면서 현재 위치 갱신
// 	queue<pair<int, int>> shark;

// 	//v는 먹을 물고기
// 	vector<pair<int, int>> fish;
// 	shark.push({ sharkY, sharkX });
	
// 	//이동거리
// 	visited[sharkY][sharkX] = 1;
// 	ateFlag = false;

// 	while (!shark.empty()) {
// 		int qSize = shark.size();

// 		//현재위치에서 먹을 물고기위치 찾으면서 그 곳까지 최소거리 구하기
// 		while (qSize--) {
// 			int row = shark.front().first;
// 			int column = shark.front().second;
// 			shark.pop();
// 			for (int i = 0; i < 4; i++) {
// 				int nR = row + dr[i];
// 				int nC = column + dc[i];
// 				/*
// 				새로운 위치 ny,nx가 map의 범위에 있는지 체크하고
// 				최소 거리를 구하기위해서는 갔던 길을 또 가면 안되기 때문에 누적 거리 있는지 체크 누적 거리가 있다면 방문 한적이 있는 것
// 				(visited[ny][nx] == 0)
// 				*/
// 				if (nR >= 0 && nC >= 0 && nR < n && nC < n && visited[nR][nC] == 0) {
// 					if (map[nR][nC] == 0 || map[nR][nC] == sharkSize) { // 상어가 이동 가능
// 						shark.push({ nR, nC });
// 						visited[nR][nC] = visited[row][column] + 1;
// 					}
// 					else if (map[nR][nC] < sharkSize) { // 물고기를 만남
// 						fish.push_back({ nR, nC });
// 						visited[nR][nC] = visited[row][column] + 1;
// 					}
// 				}
// 			}
// 		}

// 		if (fish.size() >= 1) { // 먹을 수 있는 물고기가 여러마리일 때
// 			//vector 정렬 하면 y,x순으로 오름차순 정렬 되므로 문제의 조건에 맞게 0번 인덱스는 가장 위, 왼쪽 위치가 된다.
// 			sort(fish.begin(), fish.end());
// 			map[fish[0].first][fish[0].second] = 0;
// 			ateFlag = true;
// 			sharkY = fish[0].first;
// 			sharkX = fish[0].second;
// 			++ateCnt;
// 			//누적 거리에서 초기 위치를 1로 시작햇으므로 -1해줌
// 			answerTime += visited[fish[0].first][fish[0].second] - 1;
// 			break;
// 		}
// 	}
// }

// int main() {
// 	freopen("input.txt", "rt", stdin);

// 	//입력, 상어위치 저장
// 	scanf("%d", &n);
// 	for (int i = 0; i < n; i++) {
// 		for (int j = 0; j < n; j++) {
// 			scanf("%d", &map[i][j]);
// 			if (map[i][j] == 9) {
// 				sharkY = i;
// 				sharkX = j;
// 				map[i][j] = 0;
// 			}
// 		}
// 	}

// 	while (1) {
// 		//조건에 맞게 물고기 먹기
// 		bfs();
// 		//빠져 나온 후 물고기 위치에서 다시 BFS 수행
// 		memset(visited, 0, sizeof(visited));
// 		if (ateFlag == false) break;
// 		else if (ateCnt == sharkSize) {
// 			++sharkSize;
// 			ateCnt = 0;
// 		}
// 	}
// 	printf("%d", answerTime);

// }


// #include <iostream>
// #include <queue>
// #include <algorithm>
// #include <cstring>
// #include <vector>

// int map[21][21];
// int visited[21][21];
// int dy[4] = { -1,0,0,1 };
// int dx[4] = { 0,-1,1,0 };
// int size = 2;
// int n;
// int sharkY;
// int sharkX;
// int ate;
// int time;
// bool ateFlag = false;

// void createMap() {
// 	std::cin >> n;
// 	for (int i = 0; i < n; i++) {
// 		for (int j = 0; j < n; j++) {
// 			std::cin >> map[i][j];
// 			if (map[i][j] == 9) {
// 				sharkY = i;
// 				sharkX = j;
// 				map[i][j] = 0;
// 			}
// 		}
// 	}
// }

// void bfs() {
//     //이동하면서 현재 위치 갱신
// 	std::queue<std::pair<int, int>>q;
//     //v는 먹을 물고기
// 	std::vector<std::pair<int, int>>v;
// 	q.push({ sharkY, sharkX });
//     //이동거리
// 	visited[sharkY][sharkX] = 1;
// 	ateFlag = false;

// 	while (!q.empty()) {
// 		int qSize = q.size();
// 		while (qSize--) {
// 			int y = q.front().first;
// 			int x = q.front().second;
// 			q.pop();
// 			for (int i = 0; i < 4; i++) {
// 				int ny = y + dy[i];
// 				int nx = x + dx[i];
//                 /*
//                 새로운 위치 ny,nx가 map의 범위에 있는지 체크하고
//                 최소 거리를 구하기위해서는 갔던 길을 또 가면 안되기 때문에 누적 거리 있는지 체크 누적 거리가 있다면 방문 한적이 있는 것
//                 (visited[ny][nx] == 0)
//                 */ 
// 				if (ny >= 0 && nx >= 0 && ny < n && nx < n && visited[ny][nx] == 0) {
// 					if (map[ny][nx] == 0 || map[ny][nx] == size) { // 상어가 이동 가능
// 						q.push({ ny, nx });
// 						visited[ny][nx] = visited[y][x] + 1;
// 					}
// 					else if (map[ny][nx] < size) { // 물고기를 만남
// 						v.push_back({ ny, nx });
// 						visited[ny][nx] = visited[y][x] + 1;
// 					}
// 				}
// 			}
// 		}
        
// 		if (v.size() >= 1) { // 먹을 수 있는 물고기가 여러마리일 때
// 			//vector 정렬 하면 y,x순으로 오름차순 정렬 되므로 문제의 조건에 맞게 0번 인덱스는 가장 위, 왼쪽 위치가 된다.
//             std::sort(v.begin(), v.end());
// 			map[v[0].first][v[0].second] = 0;
// 			ateFlag = true;
// 			sharkY = v[0].first;
// 			sharkX = v[0].second;
// 			ate++;
//             //누적 거리에서 초기 위치를 1로 시작햇으므로 -1해줌
// 			time += visited[v[0].first][v[0].second] - 1;
// 			break;
// 		}
// 	}
// }

// int main() {
// 	createMap();
// 	while (1) {
//         //조건에 맞게 물고기 먹기
// 		bfs();
//         //빠져 나온 후 물고기 위치에서 다시 BFS 수행
// 		memset(visited, 0, sizeof(visited));
// 		if (ateFlag == false) break;
// 		else if (ate == size) {
// 			size++;
// 			ate = 0;
// 		}
// 	}
// 	std::cout << time;
// }



// # https://www.acmicpc.net/problem/16236
// '''
// *  저장을 어떻게 할 것이냐
// - 물고기 : 위치, 크기  ex) A[r][c] == 물고기의 크기 // 물고기가 없는 경우는 0을 넣는다 
// - 상어   : 위치, 크기, 경헙치( 지금까지 먹은 물고기의 개수 -> 크기가 변하면 0으로 )
// - 공간   : 물고기, 상어

// * 변하는 값, 변하지 않는 값
// 변하지 않는 값 : 물고기위치, 물고기크기, 
// 변하는 값 : 상어의 위치 , 상어의 크기 

// --1) 이동할 때마다, 

// * 이동 ( 아래 반복 ) 
// 1) 상어가 먹을 수 있는 물고기를 찾고
// - 거리가 가장 가까운 물고기를 먹는다 ( 격자형태에서의 최소값 = BFS , 걸리는 시간 = N^2 : 거리가 가장
// 가까운 상어를 찾았다고 해서, 그것이 하나는 아니니까. 즉, 상어와 물고기 사이의 '모든' 거리를 다 구해주고 
// 그 다음에 비로소, 최소를 찾으려고 한다 )
// - 즉, 1_1) 물고기까지의 거리 , 1_2) 물고기의 위치 ( 왼쪽, 위를 먼저 먹으니까 )
// 2) 이동해서 먹는다 

// 모든 칸에 물고기가 있고, 상어가 이 물고기를 모두 먹을 수 있다면
// 각 칸에서, 모든 물고기까지의 거리, 위치를 파악하는 BFS를 수행

// 즉, BFS는 N^2
// 그것을 모든 격자에서 수행 N^2
// 따라서 O( N ^ 4 )
// '''
// from collections import deque
// dx = [0, 0, 1, -1]
// dy = [1, -1, 0, 0]


// def bfs(a, x, y, size):
//     n = len(a)
//     ans = []
//     d = [[-1]*n for _ in range(n)]
//     q = deque()
//     q.append((x, y))
//     d[x][y] = 0
//     while q:
//         x, y = q.popleft()
//         for k in range(4):
//             nx, ny = x+dx[k], y+dy[k]
//             if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
//                 # 1) 먹을 수 있는 애 : 사이즈 작은 애
//                 # 2) 갈수만 있는애 : 같은 애들 , 빈칸
//                 # 3) 그외 : 큰 애들 : x

//                 ok = False  # 갈 수 있냐
//                 eat = False  # 먹을 수 있냐
//                 # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
//                 if a[nx][ny] == 0:
//                     ok = True
//                 elif a[nx][ny] < size:  # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
//                     ok = True
//                     eat = True
//                 # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
//                 elif a[nx][ny] == size:
//                     ok = True
//                 if ok:
//                     q.append((nx, ny))
//                     d[nx][ny] = d[x][y] + 1
//                     if eat:
//                         # ans에 넣어주는 순서가 매우 중요하다
//                         ans.append((d[nx][ny], nx, ny))
//                         # 먹을 수 있는 물고기의 정렬 우선 순위는 다음과 같다
//                         # 1) 거리
//                         # 2) 행 ( 맨 위 )
//                         # 3) 열 ( 맨 왼쪽)
//                         # 이를 있는 그대로 반영하기 위해 위와 같은 원소의 순서로 ans에 넣어주어야 한다
//     if not ans:
//         return None
//     ans.sort()
//     return ans[0]


// n = int(input())
// a = [list(map(int, input().split())) for _ in range(n)]
// x, y = 0, 0
// for i in range(n):
//     for j in range(n):
//         if a[i][j] == 9:
//             x, y = i, j
//             a[i][j] = 0
// ans = 0
// size = 2
// exp = 0
// while True:
//     p = bfs(a, x, y, size)
//     if p is None:
//         break
//     dist, nx, ny = p
//     a[nx][ny] = 0
//     ans += dist
//     exp += 1
//     if size == exp:
//         size += 1
//         exp = 0
//     x, y = nx, ny  # 아기 상어 이동 처리
// print(ans)


// '''
// C++

// #include <iostream>
// #include <algorithm>
// #include <queue>
// #include <tuple>
// #include <vector>
// using namespace std;
// int dx[] = {0,0,1,-1};
// int dy[] = {1,-1,0,0};
// tuple<int,int,int> bfs(vector<vector<int>> &a, int x, int y, int size) {
//     int n = a.size();
//     vector<tuple<int,int,int>> ans; // "모든" 물고기까지의 거리 및 위치 정보 저장 --> "거리 , 행, 열"이 가장 낮은 물고기부터 먹어야 --> 모두 구해놓고 , 정렬 실시 
//     vector<vector<int>> d(n, vector<int> (n, -1)); // 거리 배열 
//     queue<pair<int,int>> q; // 큐 
//     q.push(make_pair(x,y));
//     d[x][y] = 0;
//     while (!q.empty()) {
//         tie(x,y) = q.front();
//         q.pop();
//         for (int k=0; k<4; k++) { // 상어가, 인접한 nx, ny로 이동하는 경우 
//             int nx = x+dx[k];
//             int ny = y+dy[k];
//             if (0 <= nx && nx < n && 0 <= ny && ny < n && d[nx][ny] == -1) { // 범위 내에 존재 + 방문한 적이 없어야 한다 
//                 bool ok = false;
//                 bool eat = false;
//                 // 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
//                 if (a[nx][ny] == 0) { // 이동하려는 칸이 빈칸이면 이동하기 
//                     ok = true; // 먹을수는 없으니, 이동만 할 수 있다고 해주기 
//                 } else if (a[nx][ny] < size) { // 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
//                     ok = eat = true;
//                 } else if (a[nx][ny] == size) { // 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
//                     ok = true;
//                 }
//                 if (오케이) {
//                     q.push(make_pair(nx,ny));
//                     d[nx][ny] = d[x][y] + 1;
//                     if (eat) {
//                         ans.push_back(make_tuple(d[nx][ny],nx,ny)); // 먹을 수 있는 경우에만, 거리, 행 ,열. 정보를 넣어준다 
//                     }
//                 }
//             }
//         }
//     }
//     if (ans.empty()) {
//         // 먹을 수 있는 물고기가 없다면, dist를 -1 리턴해준다 
//         return make_tuple(-1,-1,-1);
//     }
//     // 정렬 
//     sort(ans.begin(), ans.end());
//     // 제일 첫번째 return == 문제조건에 따라 ~ 거리 제일 작고, 행과 열도 가장 작은 것 
//     return ans[0];
// }
// int main() {
//     int n;
//     cin >> n;
//     vector<vector<int>> a(n, vector<int>(n, 0));
//     int x, y; // 상어의 위치 -> 계속 바뀔 수 있다 
//     for (int i=0; i<n; i++) {
//         for (int j=0; j<n; j++) {
//             cin >> a[i][j];
//             if (a[i][j] == 9) { // a[i][j]는 물고기의 크기 --> a[i][j]가 9 라는 것은, 상어가 해당 위치에 있다는 것이므로, 
//                 tie(x, y) = make_pair(i, j); // 상어의 위치는 별도로 저장을 하고 
//                 a[i][j] = 0; // 해당 위치를 0으로 만들어준다( 물고기가 없다 )
//             }
//         }
//     }
//     int ans = 0; // 시간 
//     int size = 2; // 상어의 크기 
//     int exp = 0;  // 경험치 ( 지금까지 먹은 물고기의 개수 )
//     while (true) {
//         int nx, ny, dist;
//         tie(dist,nx,ny) = bfs(a, x, y, size);  // 거리, 행, 열 정보를 return 
//         if (dist == -1) break;  // 더이상 먹을 수 있는 물고기가 없을 때 
//         a[nx][ny] = 0;          // 해당 위치의 물고기를 먹으면 0으로 만들어준다 
//         ans += dist;            // 물고기까지의 거리가, 이동거리의 합, 엄마 상어에게 도움 요청안하고 물고기 잡아먹을 수 있는 시간과 같다. 따라서, 정답에 거리를 더해주고 
//         exp += 1;               // 먹은 물고기의 개수를 1 증가시켜준다 
//         if (size == exp) {      // 상어 크기와 먹은 물고기의 개수가 같으면, 상어 크기를 증가시키고, 경험치 reset 
//             size += 1;
//             exp = 0;
//         }
//         tie(x,y) = make_pair(nx,ny); // 상어의 위치를 먹은 물고기의 위치로 바꿔준다 
//     }
//     cout << ans << '\n';
//     return 0;
// }


// '''