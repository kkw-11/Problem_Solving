//////27. N!의 표현법
//#include<stdio.h>
//#include<stdlib.h>
//
//int main() {
//	int n, temp;
//	scanf("%d", &n);
//	int* p = (int*)calloc(n + 1, sizeof(int));
//
//	for (int i = 2; i <= n; ++i) {
//		temp = i;
//		int j = 2;
//
//		while (j <= n && temp != 1) {
//			if (temp % j == 0) {
//				++p[j];
//				temp /= j;
//			}
//			else
//				++j;
//		}
//	}
//
//	printf("%d! = ", n);
//	
//	for (int i = 2; i <= n; ++i) {
//		if (p[i] != 0) {
//			printf("%d ", p[i]);
//
//		}
//	}
//	free(p);
//
//	return 0;
//}

////27. N!의 표현법
//#include <stdio.h>
//#include <stdlib.h>
//int Factorial(int x) {
//	if (x == 1) return 1;
//
//	return x * Factorial(x - 1);
//}
//bool Primenumber(int x) {
//	int i = 2;
//	for (i = 2; i < x/2; ++i) {
//		if (x % i == 0)break;
//	}
//	if (i == x) return 1;
//	else return 0;
//}
//
//int main() {
//	int n;
//	int num;
//	int game = 1;
//	int prime[1001] = { -1,-1,0 };
//	for (int i = 2; i < 1001; ++i) {
//		if (Primenumber(i)) prime[i] = 0;
//		else prime[i] = -1;
//	}
//
//
//	//숫자 입력
//	scanf("%d", &n);
//
//	//입력된 값 팩토리얼 구하기
//	num = Factorial(n);
//
//	//팩토리얼을  소수별로 나누어 보면서 나누어 떨어지면 해당 소수 카운트 증가시키키
//	for (int i = 2; i <= n; ++i) {
//		if (Primenumber(i))
//			while (!(num % i)) {
//				++prime[i];
//				num /= i;
//			}
//	}
//
//	/*for (int i = 0; i <= n; ++i) {
//		printf("prime[%d]:%d\n", i, prime[i]);
//	}*/
//
//
//	//소수개수 몇개 필요한지 출력하기
//
//	printf("%d! = ", n);
//	for (int i = 2; i <= n; ++i) {
//		if (prime[i] != -1) {
//			printf("%d ", prime[i]);
//		}
//	}