//29.3의 개수는?(small)
#include <stdio.h>
int main() {
	freopen("input.txt", "rt", stdin);
	int n, temp, cnt = 0;
	scanf("%d", &n);
	int temp2 = 10;

	for (int i = 1; i <= n; ++i) {
		temp = i;
		while (temp > 0) {
			if (temp % 10 == 3) {
				++cnt;
			}

			temp /= 10;
		}
		if (i == temp2) {
			printf("number:%d->%d\n", i, cnt);
			temp2 *= 10;
		}
		/*if (i <= 10000) {
			if (i == temp2) {
				printf("number:%d->%d\n", i, cnt);
				temp2 *= 10;
			}
		}
		else {
			if(i % 10000 ==0)
				printf("number:%d->%d\n", i, cnt);

		}*/

	}
	printf("%d", cnt);
	return 0;


}



////29.3의 개수는?(small)
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, temp, cnt = 0;
//	scanf("%d", &n);
//
//	for (int i = 1; i <= n; ++i) {
//		temp = i;
//		while (temp != 0) {
//			if (temp % 10 == 3) {
//				++cnt;
//			}
//			temp /= 10;
//		}
//
//	}
//	printf("%d", cnt);
//	////자리수 구하기
//	//while (temp != 0) {
//	//	temp /= 10;
//	//	++digit;
//	//}
//
//	return 0;
//
//}
//