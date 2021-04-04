//48. 각 행의 평균과 가장 가까운 값
#include <stdio.h>
#include <math.h>
int main() {
//	freopen("input.txt", "rt", stdin);
	int num[9][9];
	int avg[9];
	int sum,cursub, minsub, minsubnum;

	for (int i = 0; i < 9; ++i) {
		sum = avg[i] = 0;
		int j;
		for (j = 0; j < 9; ++j) {
			scanf("%d", &num[i][j]);
			sum += num[i][j];
		}
		avg[i] = round((double)sum /(double)j);
//		printf("sum: %d, avg:%d\n", sum,avg[i]);
	}

	for (int i = 0; i < 9; ++i) {
		minsubnum = num[i][0];
		minsub = avg[i] - num[i][0];
		if (minsub < 0) minsub = -minsub;


		for (int j = 0; j < 9; ++j) {
			cursub = avg[i] - num[i][j];
			if (cursub < 0) cursub = -cursub;

			if (minsub > cursub) {
				minsub = cursub;
				minsubnum = num[i][j];
			}

			if (minsub == cursub) {
				if (minsubnum < num[i][j])
					minsubnum = num[i][j];
			}

		}
		printf("%d %d\n", avg[i], minsubnum);
	}


	return 0;
}
