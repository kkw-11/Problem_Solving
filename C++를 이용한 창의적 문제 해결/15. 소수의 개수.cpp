////15. 소수의 개수
//bool isPrime(int x) {
//	if (x == 1) return 0;
//	bool prime = true;
//	for (int i = 2; i*i <= x; ++i) {
//		if (x % i == 0) {
//			prime = false;
//			break;
//		}
//	}
//
//	return prime;
//}
//
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	int n, cnt = 0;
//	scanf("%d", &n);
//
//	//1~n까지 소수 개수 구하기
//	for (int i = 2; i <= n; ++i) {
//		//i가 소수이면 1 증가
//		if (isPrime(i)) {
//			++cnt;
//		}
//	}
//
//	printf("%d", cnt);
//
//	return 0;
//}
//
////15. 소수의 개수
//bool isPrime(int x) {
//	if (x == 1) return 0;
//	bool prime = true;
//	for (int i = 2; i < x; ++i) {
//		if (x % i == 0) {
//			prime = false;
//			break;
//		}
//	}
//
//	return prime;
//}
//
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	int n, cnt = 0;
//	scanf("%d", &n);
//
//	//1~n까지 소수 개수 구하기
//	for (int i = 2; i <= n; ++i) {
//		//i가 소수이면 1 증가
//		if (isPrime(i)) {
//			++cnt;
//		}
//	}
//
//	printf("%d", cnt);
//
//	return 0;
//}


////15. 소수의 개수
//bool isPrime(int x) {
//	if (x == 1) return 0;
//	bool prime = true;
//	for (int i = 2; i < x; ++i) {
//		if (x % i == 0) {
//			prime = false;
//			break;
//		}
//	}
//
//	return prime;
//}
//
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	int n, cnt = 0, num[30000];
//	scanf("%d", &n);
//	
//	//숫자 배열에 저장
//	for (int i = 0; i <= n; ++i) {
//		num[i] = i;
//	}
//
//	//1~n까지 소수 개수 구하기
//	for (int i = 2; i <= n; ++i) {
//		//i가 소수이면 1 증가
//		if (isPrime(num[i])) {
//			++cnt;
//			//i의 배수는 모두 1로 만들기
//			for (int j = 2; j * i <= n; ++j) {
//				num[i*j] = 1;
//			}
//		}
//	}
//
//	printf("%d", cnt);
//
//	return 0;
//}

////15. 소수의 개수
//bool isPrime(int x) {
//	if (x == 1) return 0;
//	bool prime = true;
//	for (int i = 2; i < x; ++i) {
//		if (x % i == 0) {
//			prime = false;
//			break;
//		}
//	}
//
//	return prime;
//}
//
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	int n, cnt = 0;
//	scanf("%d", &n);
//	int* p = (int*)malloc(sizeof(int) * (n + 2));
//	for (int i = 0; i <= n; ++i) {
//		p[i] = i;
//	}
//
//	for (int i = 2; i <= n; ++i) {
//		for (int j = i + 1; j <= n; ++j) {
//			if (p[j] == 0) break;
//			if (p[j] % i == 0) {
//				p[j] = 0;
//			}
//		}
//	}
//
//	//1~n까지 소수 개수 구하기
//	for (int i = 2; i <= n; ++i) {
//		//i가 소수이면 1 증가
//		if (p[i] != 0 && isPrime(i)) ++cnt;
//
//	}
//
//	printf("%d", cnt);
//	free(p);
//
//	return 0;
//}