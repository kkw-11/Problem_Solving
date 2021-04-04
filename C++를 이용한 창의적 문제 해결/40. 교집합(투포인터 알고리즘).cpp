//40.교집합(투포인터 알고리즘)
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	//	freopen("input.txt", "rt", stdin);
	int n, m;
	scanf("%d", &n);
	vector<int> a(n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &a[i]);
	}
	sort(a.begin(), a.end());

	scanf("%d", &m);
	vector<int> b(m);
	for (int i = 0; i < m; ++i) {
		scanf("%d", &b[i]);
	}
	sort(b.begin(), b.end());

	int i = 0, j = 0, k =0;
	while (i < n && j < m) {
		if (a[i] < b[j])
			++i;
		else if (a[i] > b[j])
			++j;
		else {
			printf("%d ", a[i]);
			++i;
			++j;
		}
	}

	return 0;
}

//
////40.교집합(투포인터 알고리즘)
//#include <stdio.h>
//#include <stdlib.h>
//void swap(int* a, int* b) {
//	int temp = *a;
//	*a = *b;
//	*b = temp;
//}
//
//void sort(int arr[], int size) {
//	for (int i = size; i > 1; --i) {
//		int j;
//		for (j = 0; j < i - 1; ++j) {
//			if (arr[j] > arr[j + 1]) {
//				swap(&arr[j], &arr[j + 1]);
//			}
//		}
//	}
//}
//
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, m;
//	int* a, *b;
//	scanf("%d", &n);
//	a = (int*)malloc(sizeof(int) * n);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &a[i]);
//	}
//	sort(a, n);
//
//	scanf("%d", &m);
//
//	b = (int*)malloc(sizeof(int) * m);
//	for (int i = 0; i < m; ++i) {
//		scanf("%d", &b[i]);
//	}
//
//	sort(b, m);
//
//	int i = 0, j = 0;
//	while (i < n && j < m) {
//		if (a[i] < b[j])
//			++i;
//		else if (a[i] > b[j])
//			++j;
//		else {
//			printf("%d ", a[i]);
//			++i;
//			++j;
//		}
//	}
//
//	return 0;
//}
////40.교집합(투포인터 알고리즘)
//#include <stdio.h>
//void swap(int* a, int* b) {
//	int temp = *a;
//	*a = *b;
//	*b = temp;
//}
//
//void sort(int arr[], int size) {
//	for (int i = size; i > 1; --i) {
//		int j;
//		for (j = 0; j < i - 1; ++j) {
//			if (arr[j] > arr[j + 1]) {
//				swap(&arr[j], &arr[j + 1]);
//			}
//		}
//	}
//}
//int main() {
////	freopen("input.txt", "rt", stdin);
//	int n, m;
//	int a[30000], b[30000];
//	scanf("%d", &n);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &a[i]);
//	}
//	sort(a, n);
//
//	scanf("%d", &m);
//
//	for (int i = 0; i < m; ++i) {
//		scanf("%d", &b[i]);
//	}
//
//	sort(b, m);
//
//	int i = 0, j = 0;
//	while (i < n && j < m) {
//		if (a[i] < b[j])
//			++i;
//		else if (a[i] > b[j])
//			++j;
//		else {
//			printf("%d ", a[i]);
//			++i;
//			++j;
//		}
//	}
//
//	return 0;
//}


////40.교집합(투포인터 알고리즘)
//#include <stdio.h>
//void swap(int* a, int* b) {
//	int temp = *a;
//	*a = *b;
//	*b = temp;
//}
//void sort(int arr[], int size) {
//	for (int i = size; i > 1; --i) {
//		int j;
//		for (j = 0; j < i - 1; ++j) {
//			if (arr[j] > arr[j + 1]) {
//				swap(&arr[j], &arr[j + 1]);
//			}
//		}
//	}
//}
//int main() {
//	int n, m;
//	int a[30000], b, c[30000];
//	scanf("%d", &n);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &a[i]);
//	}
//	scanf("%d", &m);
//
//	//b값 받으면서 a랑 중복값 찾기
//	int k = 0;
//	for (int i = 0; i < m; ++i) {
//		scanf("%d", &b);
//		for (int j = 0; j < n; ++j) {
//			if (b == a[j]) {
//				c[k++] = b;
//				break;
//			}
//
//		}
//	}
//
//	//c 내림차순 정렬하면서 출력
//	for (int i = k; i > 1; --i) {
//		int j;
//		for (j = 0; j < i - 1; ++j) {
//			if (c[j] < c[j + 1]) {
//				swap(&c[j], &c[j + 1]);
//			}
//		}
//		printf("%d ", c[j]);
//	}
//	printf("%d", c[0]);
//
//	/*for (int i = 0; i < k; ++i) {
//		printf("%d ", c[i]);
//	}*/
//
//
//	return 0;
//}

//
////40.교집합(투포인터 알고리즘)
//#include <stdio.h>
//void swap(int* a, int* b) {
//	int temp = *a;
//	*a = *b;
//	*b = temp;
//}
//int main() {
//	int n, m;
//	int a[30000], b, c[30000];
//	scanf("%d", &n);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &a[i]);
//	}
//	scanf("%d", &m);
//
//	//b값 받으면서 a랑 중복값 찾기
//	int k = 0;
//	for (int i = 0; i < m; ++i) {
//		scanf("%d", &b);
//		for (int j = 0; j < n; ++j) {
//			if (b == a[j]){
//				c[k++] = b;
//				break;
//			}
//
//		}
//	}
//
//	//c 내림차순 정렬하면서 출력
//	for (int i = k; i > 1; --i) {
//		int j;
//		for (j = 0; j < i - 1; ++j) {
//			if (c[j] <	c[j + 1]) {
//				swap(&c[j], &c[j + 1]);
//			}
//		}
//		printf("%d ", c[j]);
//	}
//	printf("%d", c[0]);
//
//	/*for (int i = 0; i < k; ++i) {
//		printf("%d ", c[i]);
//	}*/
//
//
//	return 0;
//}
//