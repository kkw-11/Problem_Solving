//71. 송아지 찾기(BFS : 상태트리탐색)
#include <stdio.h>
#include <queue>
#include <algorithm>
using namespace std;
int main() {
	freopen("input.txt", "rt", stdin);
	int s, e, x, nx;
	scanf("%d %d", &s, &e);
	
	
	int checkCnt[10001] = {0,};
	int dirx[] = { -1,1,5 };
	queue<int> Q;

	Q.push(s);
	checkCnt[s] = 1;

	while (!Q.empty()) {
		x = Q.front();
		Q.pop();
		for (int dir = 0; dir < 3; ++dir) {
			nx = x + dirx[dir];

			if (nx <= 0 || nx > 10000)
				continue;
			if (nx == e) {
				printf("%d", checkCnt[x]);
				exit(0);
			}
			if(checkCnt[nx] == 0){	
				Q.push(nx);
				checkCnt[nx] = checkCnt[x] + 1;
			}
		}

	}

	return 0;
}

// //71. 송아지 찾기(BFS : 상태트리탐색)
////함수로 코드 리팩토링
// #include <stdio.h>
// #include <queue>
// #include <algorithm>
// using namespace std;
// void BFS(int s,int e) {
// 	int checkCnt[10001] = { 0, };
// 	int dirX[] = { -1,1,5 };
	
// 	queue<int> Q;
// 	Q.push(s);
// 	checkCnt[s] = 1;

// 	while (!Q.empty()) {
// 		int x = Q.front();
// 		Q.pop();
// 		for (int dir = 0; dir < 3; ++dir) {
// 			int nx = x + dirX[dir];
// 			if (nx <= 0 || nx > 10000) continue;
// 			if (nx == e) {
// 				printf("%d", checkCnt[x]);
// 				exit(0);
// 			}

// 			if (checkCnt[nx] == 0) {
// 				Q.push(nx);
// 				checkCnt[nx] = checkCnt[x] + 1;
// 			}
// 		}

// 	}

// }

// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	int s, e, x, nx;

// 	scanf("%d %d", &s, &e);

// 	BFS(s,e);

// 	return 0;
// }



// //직관적 풀이
// #include <stdio.h>
// #include <algorithm>
// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	int s, e, delta = 0, cnt = 0;
// 	scanf("%d %d", &s, &e);

// 	if (s < e) {
// 		while (1) {
// 			if (abs(e - s) <= 3) {
// 				delta = abs(e - s);
// 				cnt += delta;
// 				break;
// 			}
// 			else {
// 				s += 5;
// 				++cnt;
// 			}

// 			if (s == e)
// 				break;

// 		}
// 	}
// 	else if (s > e) {
// 		cnt = s - e;
// 	}

// 	printf("%d", cnt);
// 	return 0;
// }
