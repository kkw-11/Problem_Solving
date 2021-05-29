// //https://www.acmicpc.net/problem/16234
// //DFS 풀이, 인구총합을 return 값으로 처리하지 않고 전역변수로 풀이
#include<stdio.h>
#include<algorithm>
int n, r, l;
int map[50][50];
int check[50][50]; //0방문 안함, 1동맹국, 2인구갱신완료
//int dirR[] = { -1,1,0,0 };
//int dirC[] = { 0,0,-1,1 };
int total, cnt, sum;

void go(int row, int column, int prevalue) {
	
	if (row < 0 || row >= n || column < 0 || column >= n) return;
	if (check[row][column]) return;//현재 (row,column)이 방문했으면 리턴
	//이전값이 없을 경우 prevalue = -1 로 체크 차를 비교할 수 없기 때문에 바로 다음으로
	

	if (prevalue != -1) {
		int delta = abs(prevalue - map[row][column]);
		if (delta<l || delta>r) return;
	}

	check[row][column] = 1;
	++cnt;
	sum += map[row][column];

	go(row - 1, column, map[row][column]);
	go(row + 1, column, map[row][column]);
	go(row, column - 1, map[row][column]);
	go(row, column + 1, map[row][column]);

	//  for (int dir = 0; dir < 4; ++dir) {
	// 		int nr = r + dirR[dir];
	// 		int nc = c + dirC[dir];
	// 		population += go(nr, nc, map[r][c]);
	//  }

}
void renewal(int row, int column, int avg) {
	if (row < 0 || row >= n || column < 0 || column >= n) return;

	if (check[row][column] == 1) {
	
		check[row][column] = 2;
		map[row][column] = avg;
		
		renewal(row - 1, column, avg);
		renewal(row + 1, column, avg);
		renewal(row, column - 1, avg);
		renewal(row, column + 1, avg);

		/*for (int dir = 0; dir < 4; ++dir) {
			int nr = r + dirR[dir];
			int nc = c + dirC[dir];
			renewal(nr, nc, avg);
		}*/
	}

}

int main() {
	//freopen("input.txt", "rt", stdin);
	int answer = 0;
	scanf("%d %d %d", &n, &l, &r);

	//입력
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			scanf("%d", &map[i][j]);
		}
	}

	int flag = true;
	
	do {
		flag = false;

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (check[i][j] == 0) {
					sum = cnt = 0;
					go(i, j, -1);

					if (cnt > 1) {
						flag = true;
						renewal(i, j, sum / cnt);
					}
					else
						check[i][j] = 2;
				}
			}
		}


		if (flag) {
			++answer;
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					check[i][j] = 0;
				}
			}
		}

	} while (flag);

	printf("%d", answer);

	return 0;
}

///////////////////////////////////////////////////////////////////////////////////////
// 아래코드는 리패토링전 스터디 코드

// 


//DFS 풀이, 인구 총합을 return 값으로 반환하도록 다시 풀이
// #include<stdio.h>
//#include<algorithm>
//int n, r, l;
//int map[50][50];
//int check[50][50];//0방문 안함, 1 동맹국, 2 인구갱신완료
////int dirR[] = { -1,1,0,0 };
////int dirC[] = { 0,0,-1,1 };
//int total, cnt;
//
//int go(int row, int column, int prevalue) {
//	if (row < 0 || row >= n || column < 0 || column >= n) return 0;
//	if (check[row][column]) return 0;//현재 (row,column)이 방문했으면 리턴
//	//이전값이 없을 경우 prevalue = -1 로 체크 차를 비교할 수 없기 때문에 바로 다음으로
//	if (prevalue != -1) {
//		int delta = abs(prevalue - map[row][column]);
//		if (delta<l || delta>r) return 0;
//	}
//
//	check[row][column] = 1;
//	++cnt;
//	int population = map[row][column];
//
//	population += go(row - 1, column, map[row][column]);
//	population += go(row + 1, column, map[row][column]);
//	population += go(row, column - 1, map[row][column]);
//	population += go(row, column + 1, map[row][column]);
//
//	/* for (int dir = 0; dir < 4; ++dir) {
//		int nr = r + dirR[dir];
//		int nc = c + dirC[dir];
//		population += go(nr, nc, map[r][c]);
//	}*/
//
//
//	return population;
//}
//void renewal(int row, int column, int avg) {
//	if (row < 0 || row >= n || column < 0 || column >= n) return;
//
//	if (check[row][column] == 1) {
//		check[row][column] = 2;
//		map[row][column] = avg;
//		renewal(row - 1, column, avg);
//		renewal(row + 1, column, avg);
//		renewal(row, column - 1, avg);
//		renewal(row, column + 1, avg);
//
//
//
//		/*for (int dir = 0; dir < 4; ++dir) {
//			int nr = r + dirR[dir];
//			int nc = c + dirC[dir];
//			renewal(nr, nc, avg);
//		}*/
//	}
//
//}
//
//int main() {
//
////	freopen("input.txt", "rt", stdin);
//	int answer = 0;
//	scanf("%d %d %d", &n, &l, &r);
//	//입력
//	for (int i = 0; i < n; ++i) {
//		for (int j = 0; j < n; ++j) {
//			scanf("%d", &map[i][j]);
//		}
//	}
//
//
//	int flag = true;
//
//	do {
//		flag = false;
//
//		for (int i = 0; i < n; ++i) {
//			for (int j = 0; j < n; ++j) {
//				if (check[i][j] == 0) {
//					cnt = 0;
//					int total = go(i, j, -1);
//
//					if (cnt > 1) {
//						flag = true;
//						renewal(i, j, total / cnt);
//					}
//					else
//						check[i][j] = 2;
//				}
//			}
//		}
//
//		if (flag) {
//
//			++answer;
//			for (int i = 0; i < n; ++i) {
//				for (int j = 0; j < n; ++j) {
//					check[i][j] = 0;
//				}
//			}
//		}
//
//	} while (flag);
//
//
//	printf("%d", answer);
//
//
//	return 0;
//}

// 위에 DFS 풀이를 BFS로 변형 풀이, 구조체로 position 잡아서
// #include <stdio.h>
// #include <queue>
// #include <algorithm>
// using namespace std;

// struct POSI {
// 	int rr, cc;
// };
// int map[50][50];
// int check[50][50];
// int n, l, r;
// int sum, cnt;
// int dr[] = { -1,1,0,0 };
// int dc[] = { 0,0,-1,1 };
// bool isUpdate;

// void go(int row, int column) {
// 	queue<POSI> q;

// 	queue<POSI> s;
// 	POSI head;
// 	head.rr = row;
// 	head.cc = column;


// 	q.push(head);

// 	while (!q.empty()) {
// 		POSI cur = q.front();
// 		q.pop();

// 		POSI nw;

// 		for (int dir = 0; dir < 4; ++dir) {
// 			nw.rr = cur.rr + dr[dir];
// 			nw.cc = cur.cc + dc[dir];

// 			if (nw.rr < 0 || nw.rr >= n || nw.cc < 0 || nw.cc >= n)continue;
// 			if (check[nw.rr][nw.cc])continue;
			
// 			int delta = abs(map[nw.rr][nw.cc] - map[cur.rr][cur.cc]);
// 			if (delta <l || delta>r)continue;
			
			
// 			//여기까지 통과했으면 동맹국 존재

// 			if (cnt == 0) {
// 				check[cur.rr][cur.cc] = 1;
// 				sum += map[cur.rr][cur.cc];
// 				++cnt;
// 				s.push(cur);
// 			}

// 			check[nw.rr][nw.cc] = 1;
// 			sum += map[nw.rr][nw.cc];
// 			++cnt;

// 			q.push(nw);
// 			s.push(nw);

// 		}
// 	}

// 	if (!s.empty()) isUpdate = true;

// 	while (!s.empty()) {
// 		POSI ch = s.front();
// 		s.pop();
// 		map[ch.rr][ch.cc] = (sum / cnt);
// 		check[ch.rr][ch.cc] = 2;
// 	}

// }

// void renewal(int row, int column, int avg) {

// 	queue<POSI> q;
// 	POSI head;
// 	head.rr = row;
// 	head.cc = column;
// 	q.push(head);

// 	while (!q.empty()) {
// 		POSI cur = q.front();
// 		q.pop();
// 		check[cur.rr][cur.cc] = 2;
// 		map[cur.rr][cur.cc] = avg;
// 		POSI nw;

// 		for (int dir = 0; dir < 4; ++dir) {

// 			nw.rr = cur.rr + dr[dir];
// 			nw.cc = cur.cc + dc[dir];
// 			if (nw.rr < 0 || nw.rr >= n || nw.cc < 0 || nw.cc >= n)continue;
			
// 			if (check[nw.rr][nw.cc] == 1) {
// 				q.push(nw);
// 			}
// 		}

// 	}

// }

// int main() {
// 	int answer = 0;
// 	freopen("input.txt", "rt", stdin);

// 	scanf("%d %d %d", &n, &l, &r);

// 	for (int i = 0; i < n; ++i) {
// 		for (int j = 0; j < n; ++j) {
// 			scanf("%d ", &map[i][j]);
// 		}
// 	}

// 	do {
// 		isUpdate = false;

// 		for (int i = 0; i < n; ++i) {
// 			for (int j = 0; j < n; ++j) {
// 				if (check[i][j] == 0) {
// 					sum = cnt = 0;
// 					go(i, j);
// 				}
// 			}
// 		}

// 		if (isUpdate) {
// 			for (int i = 0; i < n; ++i) {
// 				for (int j = 0; j < n; ++j) {
// 					check[i][j] = 0;
// 				}
// 			}
// 			++answer;
// 		}

// 	} while (isUpdate);

// 	printf("%d", answer);

// 	return 0;
// }




// // BFS로 구현 풀이, 구조체로 position 잡아서
// #include <stdio.h>
// #include <algorithm>
// #include <queue>
// using namespace std;

// typedef struct position{
// 	int r, c;
// }POSI;

// int n, l, r;
// int map[50][50];

// void check_area(int sr, int sc, int area[][50],int index, int& count, int& sum) {
// /*
// 다른 시작점에서는 동맹국이 아닐지 모르지만 지금 시작점에서 다시 동맹국으로 생길지 모르기 때문에 
// main for문에서 매번 시작좌표로 함수를 호출할때 마다 모든 좌표 방문은 초기화 해주어 현재 시작 위치로부터 방문 했었은지 확인해야 한다.
// */
// 	int visited[50][50] = { 0, }; 

// 	const int dr[] = { -1, 1, 0, 0 };
// 	const int dc[] = { 0, 0, -1, 1 };

// 	//탐색진행 전 start row, start coloum을 큐에 넣기 작업
// 	queue<POSI> q; //구조체를 통해 생성한 사용자 정의형 타입, POSI라는 타입을 담을 수 있는 큐
// 	POSI head; //head에는 int r,int c가 쌍으로 있는 타입 POSI타입의 head라는 변수명을 가진 변수 선언 
// 	head.r = sr;
// 	head.c = sc;
// 	visited[sr][sc] = 1;
// 	q.push(head);

// 	while (!q.empty()) {
// 		POSI cur = q.front(); //큐에 제일 앞에 있는 POSI 타입 변수 반환
// 		q.pop();

// 		area[cur.r][cur.c] = index;

// 		++count;
// 		sum += map[cur.r][cur.c];
// 		//현재 위치(r,c)에서 문제의 조건에 부합하는 상하좌우에 위치한 곳은 전부 큐에 넣기
// 		for (int dir = 0; dir < 4; ++dir) {
// 			POSI next;
// 			next.r = cur.r + dr[dir];
// 			next.c = cur.c + dc[dir];

// 			if (next.r < 0 || next.r >= n || next.c < 0 || next.c >= n) continue; //주어진 map에서 벗어난 위치이면 다음 방향 찾기

// 			int delta = abs(map[cur.r][cur.c] - map[next.r][next.c]); //절대값 차 구하기
// 			if (visited[next.r][next.c] == 0 && l <= delta && delta <= r) {
// 				visited[next.r][next.c] = 1;
// 				q.push(next);
// 			}
// 		}
// 	}
// }


// int main(){
// 	//freopen("input.txt", "rt", stdin);

// 	scanf("%d %d %d", &n, &l, &r);
// 	for (int y = 0; y < n; ++y) {
// 		for (int x = 0; x < n; ++x) {
// 			scanf("%d", &map[y][x]);
// 		}
// 	}

// 	int result = 0;
// 	bool is_update = true;
	
// 	while (is_update) {
// 		is_update = false;

// 		int what_area[50][50] = { 0, };
// 		int area_index = 0;
// 		int area_count[2501] = { 0, }; // 50*50 = 2500개의 개별 국가 존재 가능
// 		int people_sum[2501] = { 0, };
		
// 		for (int r = 0; r < n; ++r) {
// 			for (int c = 0; c < n; ++c) {
// 				if (what_area[r][c] == 0) {
// 					++area_index;
// 					check_area(r, c, what_area, area_index, area_count[area_index], people_sum[area_index]);
// 				}
// 			}
// 		}

// 		for (int r = 0; r < n; ++r) {
// 			for (int c = 0; c < n; ++c) {
// 				int area_num = what_area[r][c];
// 				int avg = people_sum[area_num] / area_count[area_num];
// 				if (map[r][c] != avg) {
// 					map[r][c] = avg;
// 					is_update = true;
// 				}
// 			}
// 		}

// 		if (is_update) {
// 			++result;
// 		}
// 	}

// 	printf("%d\n", result);
// 	return 0;
// }

//인구이동 파이썬 풀이
// import sys
// import heapq
// import math
// from collections import deque
// sys.setrecursionlimit(100000)

// dx = [-1,1,0,0]
// dy = [0,0,-1,1]

// N,L,R = map(int,input().split())
// pp    = [list(map(int,input().split())) for _ in range(N)]
// cnt   = 0

// def go(x,y) :
//     totSum = pp[x][y]
//     totGrp = [(x,y)]
//     for k in range(4):
//         nx,ny = x+dx[k],y+dy[k]
//         if 0 <= nx < N and 0 <= ny < N :
//             if L <= abs(pp[nx][ny] - pp[x][y]) <= R and ch[nx][ny] == False :
//                 ch[nx][ny] = True
//                 tmpSum,tmpGrp = go(nx,ny)
//                 totSum += tmpSum
//                 totGrp += tmpGrp 
//     return totSum,totGrp

// while True:
//     change = False
    
//     ch    = [[False]*N for _ in range(N)]
//     befpp = [list(p) for p in pp]
    
//     for i in range(N):
//         for j in range(N):
//             if ch[i][j] == False:
//                 ch[i][j] = True
//                 psum,pgrp = go(i,j)
//                 pavg = math.floor(psum//len(pgrp))
//                 for gp in pgrp:
//                     x,y = gp
//                     pp[x][y] = pavg
//     for i in range(N):
//         for j in range(N):
//             if befpp[i][j] != pp[i][j]:
//                 change = True
//                 break
//     if not change :
//         break
//     cnt += 1
// print(cnt)