////22. 온도의 최대값
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
////	freopen("input.txt", "rt", stdin);
//
//	int N, K;
//	int sum = 0, max = -21400000;
//	scanf("%d %d", &N, &K);
//
//	int* p =(int*)malloc(sizeof(int) * N);
//	for (int i = 0; i < N; ++i) {
//		scanf("%d", &p[i]);
//		//온도값 입력 받으면서 첫번째 구간의 합 먼저 구하기
//		if (i < K)
//			sum += p[i];
//	}
//
//	max = sum;
//	//i는 더해지는 값을 기준으로 생각해서 초기값 설정
//	for (int i = K; i < N; ++i) {
//		//구간에서 하나 추가된 값과 하나전값 빼서 구간합 구하기
//		sum += (p[i] - p[i-K]);
//		if (sum > max)
//			max = sum;
//	}
//	printf("%d", max);
//	free(p);
//
//	return 0;
//}
//
//
////22. 온도의 최대값
//#include <stdio.h>
//int main() {
////	freopen("input.txt", "rt", stdin);
//
//	int N, K;
//	int temper[100000];
//	int sum = 0, max = -21400000;
//	scanf("%d %d", &N, &K);
//
//	//i는 빠지는 값을 기준으로 생각해서 초기값 설정
//
//	for (int i = 0; i < N; ++i) {
//		scanf("%d", &temper[i]);
//		//온도값 입력 받으면서 첫번째 구간의 합 먼저 구하기
//		if (i < K)
//			sum += temper[i];
//	}
//
//	max = sum;
//	for (int i = 0; i < N - K; ++i) {
//		//구간에서 하나 추가된 값과 하나전값 빼서 구간합 구하기
//		sum += (temper[K + i] - temper[i]);
//		if (sum > max)
//			max = sum;
//	}
//	printf("%d", max);
//
//	return 0;
//}
//
////22. 온도의 최대값
//#include <stdio.h>
//int main() {
//	//	freopen("input.txt", "rt", stdin);
//
//	int N, K;
//	int temper[100000];
//	int sum, max = -21400000;
//	scanf("%d %d", &N, &K);
//
//	for (int i = 0; i < N; ++i) {
//		scanf("%d", &temper[i]);
//	}
//
//	for (int i = 0; i <= N - K; ++i) {
//		sum = 0;
//		//i일부터 K일까지 온도합 구하기
//		for (int j = i; j < K + i; ++j) {
//			sum += temper[j];
//		}
//		if (sum > max)
//			max = sum;
//	}
//
//	printf("%d", max);
//
//	return 0;
//}