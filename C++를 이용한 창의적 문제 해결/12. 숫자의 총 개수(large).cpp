//12.숫자의 총 개수(large)
#include <stdio.h>
int main() {
	//freopen("input.txt", "rt", stdin);

	int d = 9, lastdigitmax = 0,i = 1;
	int n, res = 0;
	scanf("%d", &n);

	//자리수 체크 ( 직전자리최대수 + 해당자리숫자 개수)= 해당자리 최대수
	//ex) 3자리수 체크(직전자리 최대수 9 + 해당자리 숫자개수 90 = 99)
	while (lastdigitmax + d < n) {
		res = res + i * d;//직전 자리수와 사용한숫자 누적
		++i;//현재 몇자리 인지 체크
		lastdigitmax = lastdigitmax + d;
		d = d * 10;
	}

	printf("%d", res + i*(n - lastdigitmax));
	return 0;
}


////12.숫자의 총 개수(large)
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//
//
//	int d = 9;
//	int sum = 0;
//	int n, i = 1;
//	scanf("%d", &n);
//	int res = 0;
//	while (sum + d < n) {
//		res = res + (i * d);
//		sum = sum + d;//0 + 9
//		++i;//2
//		d = d * 10;// 90
//	}
//
//	res = res + (n - sum);
//	printf("%d", res);
//	return 0;
//}