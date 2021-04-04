//23. 연속 부분 증가수열
#include <stdio.h>
#include <stdlib.h>
int main() {
	freopen("input.txt", "rt", stdin);
	int n, cnt = 1, max = cnt, pre, now;
	scanf("%d", &n);

	scanf("%d", &pre);

	for (int i = 1; i < n; ++i) {
		scanf("%d", &now);
		if (pre <= now) {
			++cnt;
			if (cnt > max)
				max = cnt;
		}
		else
			cnt = 1;
		pre = now;
	}

	printf("%d", max);
	return 0;
}


////23. 연속 부분 증가수열
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	freopen("input.txt", "rt", stdin);
//	int n, cnt = 1, max = cnt, pre, now;
//	scanf("%d", &n);
//	int* p = (int*)malloc(sizeof(int) * n);
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &p[i]);
//	}
//	pre = p[0];
//	for (int i = 1; i < n; ++i) {
//		now = p[i];
//		if (pre <= now) {
//			++cnt;
//			if (max <= cnt)
//				max = cnt;
//		}
//		else {
//			cnt = 1;
//		}
//		pre = now;
//	}
//
//	printf("%d", max);
//	return 0;
//}

////23. 연속 부분 증가수열
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, cnt = 1, max = cnt;
//	scanf("%d", &n);
//	int* p = (int*)malloc(sizeof(int) * n);
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &p[i]);
//	}
//
//	for (int i = 0; i < n-1; ++i) {
//		if (p[i] <= p[i + 1]) {
//			++cnt;
//			if (max <= cnt)
//				max = cnt;
//		}
//		else {
//			cnt = 1;
//		}
//	}
//
//	printf("%d", max);
//	return 0;
//}
