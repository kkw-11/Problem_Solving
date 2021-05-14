////57. 재귀함수 이진수 출력
//#include<stdio.h>
//void D(int x) {
//	if (x == 0) return;
//	else {
//		D(x / 2);
//		printf("%d",x%2);
//	}
//}
//int main() {
//	int n;
//	scanf("%d",&n);
//
//	D(n);
//
//	return 0;
//}


////57. 재귀함수 이진수 출력
//
//#include <stdio.h>
//int size = 0;
//void Digit(int n, int digit[]) {
//	if (n <= 0)	return;
//	else {
//		digit[size++] = n % 2;
//
//		n = n / 2;
//		Digit(n, digit);
//		//printf("%d", digit[--size]);
//	}
//}
//int main() {
//
//	int n, digit[100];
//	scanf("%d", &n);
//
//	Digit(n, digit);
//	for (int i = size - 1; i >= 0; --i) {
//		printf("%d", digit[i]);
//	}
//	return 0;
//}
