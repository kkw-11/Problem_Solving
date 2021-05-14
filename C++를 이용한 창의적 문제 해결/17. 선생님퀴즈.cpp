//////17.선생님퀴즈
//#include <stdio.h>
//int totalSum(int n) {
//	int sum = 0;
//	for (int i = 1; i <= n; ++i) {
//		sum += i;
//	}
//	return sum;
//}
//
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, sum = 0, num, ans;
//	scanf("%d", &n);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d %d", &num, &ans);
//
//		sum = totalSum(num);
//
//		if (sum == ans)printf("YES\n");
//		else printf("NO\n");
//	}
//
//
//	return 0;
//}
//
//////17.선생님퀴즈
//#include <stdio.h>
//#include <stdlib.h>
//int totalSum(int n) {
//	int sum = 0;
//	for (int i = 1; i <= n; ++i) {
//		sum += i;
//	}
//	return sum;
//}
//
//int main() {
////	freopen("input.txt", "rt", stdin);
//	int n, res;
//	scanf("%d", &n);
//	int* p = (int*)malloc(sizeof(int) * 2 * n);
//
//	for (int i = 0; i < 2 * n; ++i) {
//		scanf("%d", &p[i]);
//	}
//
//	for (int i = 0; i < (2 * n - 1); i += 2) {
//		res = totalSum(p[i]);
//		if (p[i + 1] == res) printf("YES\n");
//		else printf("NO\n");
//	}
//
//
//	free(p);
//	return 0;
//}
