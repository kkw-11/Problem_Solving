////14. 뒤집은 소수
//#include <stdio.h>
//bool isPrime(int x) {
//	if (x == 1) return 0;
//	int prime = 1;
//
//	for (int i = 2; i < x; ++i) {
//		if ((x % i) == 0) {
//			prime = 0;
//			return prime;
//		}
//	}
//	return prime;
//}
//
//int reverse(int x) {
//	int res = 0, temp;
//
//	while (x > 0) {
//		temp = x % 10;
//		res = res * 10 + temp;
//		x /= 10;
//	}
//
//	return res;
//}
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, value;
//	int num[100];
//	scanf("%d", &n);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &value);
//
//		//뒤집는다.
//		value = reverse(value);
//
//		//뒤집은 값 소수 판정
//		if (isPrime(value)) {
//			printf("%d ", value);
//		}
//
//	}
//
//	return 0;
//}

////14. 뒤집은 소수
//#include <stdio.h>
//bool isPrime(int x) {
//	if (x == 1) return 0;
//	int prime = 1;
//
//	for (int i = 2; i < x; ++i) {
//		if ((x % i) == 0) {
//			prime = 0;
//			return prime;
//		}
//
//	}
//
//	return prime;
//}
//
//
//int reverse(int x) {
//	int i = 1,k, digit, res = 0,ten=1;
//	//10배수 0 없애기
//	while (1) {
//		if (x % 10 == 0) {
//			x /= 10;
//		}
//		else break;
//	}
//	digit = int (x / 10);
//
//	//자리수 구하기
//	while (digit) {
//		digit = int(digit / 10);
//		++i;
//	}
//
//	//제일 끝자리가 몇의 자리인지 표시
//	for (int j = 1; j < i; ++j) {
//		ten *= 10;
//	}
//
//	//뒤집기
//	int temp = x, mod;
//	for (int j = 0; j < i; ++j) {
//		mod = temp % 10;
//		temp = (int)temp / 10;
//
//		mod *= ten;
//		ten /= 10;
//		res += mod;
//
//	}
//
//		
//	/*	
//	while () {
//		mod = x % 10;
//
//	}*/
//
//
//	return res;
//}
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n,value;
//	int num[100];
//	scanf("%d", &n);
//	
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &value);
//	
//		//뒤집는다.
//		value = reverse(value);
//		
//		//뒤집은 값 소수 판정
//		if (isPrime(value)) {
//			printf("%d ", value);
//		}
//		
//	}
//
//	return 0;
//}