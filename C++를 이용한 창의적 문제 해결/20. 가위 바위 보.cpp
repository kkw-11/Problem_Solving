////20. 가위 바위 보
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n;
//	int a[100], b[100];
//	scanf("%d", &n);
//	//a입력
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &a[i]);
//	}
//	//b입력
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &b[i]);
//	}
//
//	for (int i = 0; i < n; ++i) {
//		//비기는 경우와 아닌경우 나누고
//		if (a[i] == b[i]) printf("D\n");
//		//a가 이기는 경우
//		else if (a[i] == 1 && b[i] == 3)printf("A\n");
//		else if (a[i] == 2 && b[i] == 1)printf("A\n");
//		else if (a[i] == 3 && b[i] == 2)printf("A\n");
//		//나머지는 B가이기는 경우
//		else printf("B\n");
//	}
//
//	return 0;
//}

////20. 가위 바위 보
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n;
//	int a[100], b[100];
//	scanf("%d", &n);
//	//a입력
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &a[i]);
//	}
//	//b입력
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &b[i]);
//	}
//
//	for (int i = 0; i < n; ++i) {
//		//비기는 경우와 아닌경우 나누고
//		//a가 1,2,3 냈을때로 비교
//		if (a[i] == b[i]) printf("D\n");
//		else {
//			if (a[i] == 1) {
//				if (b[i] == 2)printf("B\n");
//				if (b[i] == 3)printf("A\n");
//			}
//			else if (a[i] == 2) {
//				if (b[i] == 1)printf("A\n");
//				if (b[i] == 3)printf("B\n");
//			}
//			else {
//				if (b[i] == 1) printf("B\n");
//				if (b[i] == 2)printf("A\n");
//			}
//		}
//
//	}
//
//	return 0;
//}

////20. 가위 바위 보
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n;
//	int a[100], b[100];
//	scanf("%d", &n);
//	//a입력
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &a[i]);
//	}
//	//b입력
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &b[i]);
//	}
//
//	for (int i = 0; i < n; ++i) {
//		//예외 처리 가위바위보에서 숫자 큰놈이 이긴다에서 가위와 보에서 예외가 발생 예외만 먼저 적용
//		//예외 에서는 작은 값이 이김
//		if ((a[i] == 1 && b[i] == 3) || (a[i] == 3 && b[i] == 1))
//		{
//			if (a[i] < b[i])
//				printf("A\n");
//			else if (a[i] > b[i])
//				printf("B\n");
//
//		}			
//		else{
//		if (a[i] > b[i])
//			printf("A\n");
//		else if (a[i] < b[i])
//			printf("B\n");
//		else
//			printf("D\n");
//		}
//	}
//
//	return 0;
//}