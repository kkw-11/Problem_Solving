//50. 영지(territory) 선택 : (small)
#include <stdio.h>
int main() {
	//freopen("input.txt", "rt", stdin);
	int map[51][51];
	int H, W, HH, HW, area=0, maxArea = 0;

    //입력
	scanf("%d %d", &H, &W);
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) {
			scanf("%d", &map[i][j]);
		}
	}
	scanf("%d %d", &HH, &HW);

    //알고리즘

	//i,j는 누적해서 더해 갈 시작위치 값을 의미
	for (int i = 0; i <= H - HH; ++i) {
		for (int j = 0; j <= W - HW; ++j) {
			area = 0;

			//세로는 몇회, 가로는 몇회까지만 더 할지
			for (int k = 0; k < HH; ++k) {
				for (int l = 0; l < HW; ++l) {
					area += map[i + k][j + l];
				}
			}
           //for (int k = i; k <i + HH; ++k) {
			// 	for (int l = j; l <j + HW; ++l) {
			// 		area += map[k][l];
			// 	}
			// }
			if (maxArea < area) {
				maxArea = area;
			}
		}
	}

	printf("%d", maxArea);

	return 0;
}
