////24. Jolly Jumpers
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, pre, now, sub, flag = 0;
//	int subarray[100] = { 0 };
//	int j;
//
//	scanf("%d", &n);
//	scanf("%d", &pre);
//
//	for (int i = 1; i < n; ++i) {
//		scanf("%d", &now);
//		sub = now - pre;
//		if (sub < 0)
//			sub = -sub;
//
//		if (sub > 0 && sub < n && subarray[sub] == 0)
//			subarray[sub] = sub;
//		else {
//			printf("NO\n");
//			return 0;
//		}
//	
//		
//		pre = now;
//	}
//
//	printf("YES\n");
//
//	return 0;
//
//}

////24. Jolly Jumpers
//#include <stdio.h>
//#include <stdlib.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, pre, now, sub, flag = 0;
//	int subarray[100] = { 0 };
//	int j;
//
//	scanf("%d", &n);
//	scanf("%d", &pre);
//
//	for (int i = 1; i < n; ++i) {
//		scanf("%d", &now);
//		sub = now - pre;
//		if (sub < 0)
//			sub = -sub;
//
//		if (sub >= n||subarray[sub] != 0) {
//			flag = 1;
//			break;
//		}
//		if (subarray[sub] == 0) {
//				subarray[sub] = sub;
//		}
//		
//		pre = now;
//	}
//	if (flag == 0)
//		printf("YES\n");
//
//	else
//		printf("NO\n");
//
//	return 0;
//
//}
//
////24. Jolly Jumpers
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, pre, now, sub;
//	int subarray[100] = { 0 };
//	int j;
//
//	scanf("%d", &n);
//	scanf("%d", &pre);
//
//	for (int i = 1; i < n; ++i) {
//		scanf("%d", &now);
//		sub = now - pre;
//		if (sub < 0) {
//			sub = -sub;
//			subarray[sub] = sub;
//		}
//		else
//			subarray[sub] = sub;
//
//		pre = now;
//	}
//
//	for (j = 1; j < n; j) {
//		if (subarray[j] == 0)
//			break;
//	}
//
//	if (j == n)
//		printf("YES\n");
//	else
//		printf("NO\n");
//
//
//	return 0;
//}
//

