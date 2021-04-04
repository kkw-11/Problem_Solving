//48. 각 행의 평균과 가장 가까운 값
#include <stdio.h>
#include <algorithm>
#include <math.h>
int main() {
	//freopen("input.txt", "rt", stdin);
	int num[9][9];
	int avg, sum, cursub, minsub, minsubnum;
// 입력받으면서 동시에 합과 평균,가까운 값 계산하여 출력하고 다음 행입력 받기
	for (int i = 0; i < 9; ++i) {
		sum = avg = 0;
		int j;
		for (j = 0; j < 9; ++j) {
			scanf("%d", &num[i][j]);
			sum += num[i][j];
		}
		//정수/실수 => 실수
		avg = sum / (double)j + 0.5;
		minsubnum = num[i][0];
		minsub = abs(avg - num[i][0]); //abs 절대값 함수(algoritm 헤더파일에 존재)
		for (int k = 0; k < 9; ++k) {
			cursub = abs(avg - num[i][k]);
			if (minsub > cursub) {
				minsub = cursub;
				minsubnum = num[i][k];
			}
			else if (minsub == cursub) {
				if (minsubnum < num[i][k])
					minsubnum = num[i][k];

			}
		}
		printf("%d %d\n", avg, minsubnum);
	}


	return 0;
}

// //48. 각 행의 평균과 가장 가까운 값
// #include <stdio.h>
// #include <math.h>
// int main() {
// //	freopen("input.txt", "rt", stdin);
// 	int num[9][9];
// 	int avg[9];
// 	int sum,cursub, minsub, minsubnum;

// 	for (int i = 0; i < 9; ++i) {
// 		sum = avg[i] = 0;
// 		int j;
// 		for (j = 0; j < 9; ++j) {
// 			scanf("%d", &num[i][j]);
// 			sum += num[i][j];
// 		}
// 		avg[i] = round((double)sum /(double)j);
// //		printf("sum: %d, avg:%d\n", sum,avg[i]);
// 	}

// 	for (int i = 0; i < 9; ++i) {
// 		minsubnum = num[i][0];
// 		minsub = avg[i] - num[i][0];
// 		if (minsub < 0) minsub = -minsub;


// 		for (int j = 0; j < 9; ++j) {
// 			cursub = avg[i] - num[i][j];
// 			if (cursub < 0) cursub = -cursub;

// 			if (minsub > cursub) {
// 				minsub = cursub;
// 				minsubnum = num[i][j];
// 			}

// 			else if (minsub == cursub) {
// 				if (minsubnum < num[i][j])
// 					minsubnum = num[i][j];
// 			}

// 		}
// 		printf("%d %d\n", avg[i], minsubnum);
// 	}

// 	return 0;
// }
