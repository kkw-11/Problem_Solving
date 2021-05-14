////28. N!에서 0의 개수
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, temp, cnt1 = 0, cnt2 = 0;
//	scanf("%d", &n);
//
//	//2부터 n까지 소수들로 계속 나누어 보기
//	for (int i = 2; i <= n; ++i) {
//		temp = i;
//		//i가 증가할때마다 나누는 값 2로 초기화해서 다시 나누기
//		//2로 계속 나누어 지지 않을 때
//		int j = 2;
//		while (temp != 1) {
//			if (temp % j == 0) {
//				if (j == 2) ++cnt1;
//				if (j == 5) ++cnt2;
//				temp /= j;
//			}
//			else
//				++j;
//		}
//	}
//	if (cnt1 < cnt2)
//		printf("%d", cnt1);
//	else
//		printf("%d", cnt2);
//
//
//}

////28. N!에서 0의 개수
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, cnt = 0, temp;
//	scanf("%d", &n);
//	int* p = (int*)calloc(n + 1, sizeof(int));
//
//	//2부터 n까지 소수들로 계속 나누어 보기
//	for (int i = 2; i <= n; ++i) {
//		temp = i;
//		//i가 증가할때마다 나누는 값 2로 초기화해서 다시 나누기
//		//2로 계속 나누어 지지 않을 때
//		int j = 2;
//		while (temp != 1) {
//			if (temp % j == 0) {
//				++p[j];
//				temp /= j;
//			}
//			else
//				++j;
//		}
//	}
//
//	/*for (int i = 0; i <= n; ++i) {
//		printf("p[%d]:%d\n", i, p[i]);
//	}*/
//	//10의 배수이면 5와 2가 소인수로 존재해야함
//	//5와 2가 있다면 cnt증가하고 반복하기 위해 감소시킴
//	while (p[5] > 0 && p[2] > 0) {
//		++cnt;
//		--p[5];
//		--p[2];
//	}
//
//	printf("%d", cnt);
//
//}