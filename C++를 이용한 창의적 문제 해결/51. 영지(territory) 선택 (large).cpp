// //51. 영지(territory) 선택 : (large)
// #include<stdio.h>
// #include<vector>
// #include<algorithm>
// using namespace std;
// int a[701][701], dy[701][701];
// int main(){
// 	freopen("input.txt", "rt", stdin);
// 	int h, w, n, m, i, j, tmp, max=-2147000000;
// 	scanf("%d %d", &h, &w);
// 	for(i=1; i<=h; i++){
// 		for(j=1; j<=w; j++){
// 			scanf("%d", &a[i][j]);
// 			dy[i][j]=dy[i-1][j]+dy[i][j-1]-dy[i-1][j-1]+a[i][j];
// 		}
// 	}
// 	scanf("%d %d", &n, &m);
// 	for(i=n; i<=h; i++){
// 		for(j=m; j<=w; j++){
// 			tmp=dy[i][j]-dy[i-n][j]-dy[i][j-m]+dy[i-n][j-m];
// 			if(tmp>max) max=tmp;		
// 		}
// 	}
// 	printf("%d\n", max);
// 	return 0;
// }
// //51. 영지(territory) 선택 : (large)
// #include <stdio.h>
// #include <stdlib.h>
// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	int H, W, HH, HW, maxArea=0, area;
// 	int** map;
// 	int** totalAreaMap;

// 	scanf("%d %d", &H, &W);
// 	map = (int**)malloc(sizeof(int*) * (H + 1));
// 	totalAreaMap = (int**)malloc(sizeof(int*) * (H + 1));

// 	for (int i = 0; i < (H + 1); ++i) {
// 		map[i] = (int*)calloc(W + 1, sizeof(int));
// 		totalAreaMap[i] = (int*)calloc(W + 1, sizeof(int));

// 	}


// 	//입력받으면서 현재위치의 Square형태의 까지의 누적 넓이 구하기
// 	//(i,j)는 좌측 위 대각선 꼭지점
// 	for (int i = 1; i <= H; ++i) {
// 		for (int j = 1; j <= W; ++j) {
// 			scanf("%d", &map[i][j]);
// 			totalAreaMap[i][j] = totalAreaMap[i - 1][j] + totalAreaMap[i][j - 1] - totalAreaMap[i - 1][j - 1]+ map[i][j];
// 		}
// 	}
// 	scanf("%d %d", &HH, &HW);

// 	//(k,l)은 우측 아래 대각선 꼭지점
// 	for (int k = HH; k <= H; ++k) {
// 		for (int l = HW; l <= W; ++l) {
// 			area = totalAreaMap[k][l] - totalAreaMap[k][l-HW] - totalAreaMap[k-HH][l] + totalAreaMap[k-HH][l-HW];
// 			if (area > maxArea)
// 				maxArea = area;
// 		}

// 	}
// 	printf("%d\n", maxArea);

// 	return 0;
// }




// //51. 영지(territory) 선택 : (large)
// #include <stdio.h>
// #include <stdlib.h>
// int main() {
// 	freopen("input.txt", "rt", stdin);
// 	int** map;
// 	int H, W, HH, HW, firstArea = 0, curArea = 0, area = 0, maxArea = 0;

// 	//입력
// 	scanf("%d %d", &H, &W);

// 	//2차원 동적 배열 할당
// 	map = (int**)malloc(sizeof(int*) * H);
// 	for (int i = 0; i < H; ++i) {
// 		//map[i] = (int*)malloc(sizeof(int) * W);
// 		map[i] = (int*)calloc(W,sizeof(int));//동적할당 된 메모리공간을 0으로 초기화 하면서 동적할당
// 	}


// 	for (int i = 0; i < H; ++i) {
// 		for (int j = 0; j < W; ++j) {
// 			scanf("%d", &map[i][j]);
// 		}
// 	}
// 	scanf("%d %d", &HH, &HW);

// 	


// 	//i,j는 구간의 좌측 대각선 꼭지점
// 	for (int i = 0; i <= H - HH; ++i) {

// 		int j = 0;
// 		curArea = 0;
// 		//행 바뀔때마다 다시 기준 넓이 구하기
// 		for (int k = i; k < i + HH; ++k) {
// 			for (int l = j; l < j + HW; ++l) {
// 				curArea += map[k][l];
// 			}
// 		}
// 		//firstArea를 두는 이유는 다음 2중for문에서 매번 첫번째 구간의 넓이는 사라지기 때문 미리 저장하고 최대값과 비교해서 최대값을 빼야한다.

// 		firstArea = curArea;

// 		for (int j = 0; j < W - HW; ++j) {


// 			//새롭게 더해질 곳은 기준으로 부터 현수가 갖게될 가로길이 만큼 옆으로 간곳
// 			//빠져야 할 곳은 가장 좌측(기준점에서 주어진 세로높이까지의 열)모두
// 			//"행의 기준점+HW"인 더하고 기준값 빼고 기준 값 다음 열에서 같은 행위 반복
// 			//printf("(%d,%d),cur:%d\n", i, j, curArea);


// 			for (int k = 0; k < HH; ++k) {
// 				//	printf("%d\n", map[i + k][j + HW]);
// 				curArea = curArea + (map[i + k][j + HW] - map[i + k][j]);
// 			}


// 			// 최대값 구하기
// 			if (curArea > maxArea)
// 				maxArea = curArea;
// 			if (firstArea > maxArea)
// 				maxArea = firstArea;



// 		}
// 	}

// 	printf("%d", maxArea);

// 	for (int i = 0; i < H; ++i) {
// 		free(map[i]);
// 	}

// 	free(map);


// 	return 0;
// }

