//41.연속된 자연수의 합
#include<stdio.h>
int main() {
	int N, sum = 1, cnt = 0,mod,quenti;
	scanf("%d", &N);

	//i는 연속된 숫자의 개수를 의미
	//i가 2라면 연속된 숫자가 2개라는 뜻
	for (int i = 2; i < N; ++i) {
		sum += i;
		//누적된 값이 N이 된 경우는 1부터 0을 하나씩 분배해주었다고 이해하면되고
		//누적된 값이 N 을넘어선 경우는 자연수를 더했을 때 합이 N이 될 수 없다.
		if (sum > N) break;// 1부터 연속된 숫자의 합이 이미 주어진 값이 되었다면 다음 연속한 숫자를 더한경우는 이제 경우의 수가 없음
		mod = N - sum;
		if (mod % i == 0) {
			++cnt;
			quenti = mod / i;
			int j;
			for (j = 1; j < i; ++j) {
				printf("%d + ", quenti + j);
			}
			printf("%d = %d\n", quenti + j, N);
		}

	}

	printf("%d", cnt);

	return 0;
}


////41.연속된 자연수의 합
//#include<stdio.h>
//void seqPrint(int left, int right) {
//	for (int k = left; k < right; ++k) {
//		printf("%d + ", k);
//	}
//	printf("%d = ", right);
//}
//int main() {
//	int N, sum = 0, cnt = 0;
//	scanf("%d", &N);
//
//	//N-1부터 연속된 자연수를 더해서 N이 되는 수를 찾는다.
//	//찾았을 때 카운트 개수를 증가시키고
//	//연속된 자연수 개수를 출력시킨다.
//	for (int i = N - 1; i >= 1; --i) {
//		sum = 0;
//		for (int j = i; j >= 1; --j) {
//			sum += j;
//			if (sum == N) {
//				++cnt;
//
//				seqPrint(j, i);
//				printf("%d\n", N);
//
//			}
//			else if (sum > N) break;
//		}
//	}
//
//	printf("%d", cnt);
//
//	return 0;
//}

////41.연속된 자연수의 합
//#include<stdio.h>
//int main() {
//	int N, sum = 0, cnt = 0;
//	scanf("%d", &N);
//
//	//N-1부터 연속된 자연수를 더해서 N이 되는 수를 찾는다.
//	//찾았을 때 카운트 개수를 증가시키고
//	//연속된 자연수 개수를 출력시킨다.
//	for (int i = N - 1; i >= 1; --i) {
//		sum = 0;
//		for (int j = i; j >= 1; --j) {
//			sum += j;
//			if (sum == N) {
//				++cnt;
//
//				for (int k = j; k < i; ++k) {
//					printf("%d + ", k);
//				}
//				printf("%d = %d\n", i, N);
//			}
//
//			else if (sum > N) break;
//		}
//	}
//
//	printf("%d", cnt);
//
//	return 0;
//}
