//47.봉우리(2차원 배열 탐색)
#include<stdio.h>
//전역 변수로 선언하면 자동으로 초기값 0 
int map[52][52];
int dx[] = { 0,0,-1,1 };
int dy[] = { -1,1,0,0 };
int main() {
	//freopen("input.txt", "rt", stdin);

	int n;
	int cnt = 0;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			scanf("%d", &map[i][j]);
		}
	}
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			int flag = 0;
			for (int k = 0; k < 4; ++k) {
				//중심점 기순 상하좌우 한 곳이라도 큰 곳 있으면 검사 종료 및 체크
				if (map[i][j] <= map[i + dx[k]][j + dy[k]]) {
					flag = 1;
					break;
				}
			}
			//체크한적 없으면 카운트값 증가
			if (flag == 0)
				++cnt;
		}
	}

	printf("%d", cnt);


	return 0;
}
//
//////47.봉우리(2차원 배열 탐색)
//#include<stdio.h>
////전역 변수로 선언하면 자동으로 초기값 0 
//int map[52][52];
//int main() {
//	//freopen("input.txt", "rt", stdin);
//
//	int n;
//	int cnt = 0;
//	scanf("%d", &n);
//	for (int i = 1; i <= n; ++i) {
//		for (int j = 1; j <= n; ++j) {
//			scanf("%d", &map[i][j]);
//		}
//	}
//
//	for (int i = 1; i <= n; ++i) {
//		for (int j = 1; j <= n; ++j) {
//			if ((map[i][j] > map[i - 1][j]) && (map[i][j] > map[i + 1][j]) && (map[i][j] > map[i][j - 1]) && (map[i][j] > map[i][j + 1]))
//				++cnt;
//		}
//	}
//
//	printf("%d", cnt);
//
//
//	return 0;
//}
