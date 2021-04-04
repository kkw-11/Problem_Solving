//34 버블정렬
#include <stdio.h>

void Swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void PrintArray(int arr[], int size) {
	for (int i = 0; i < size; ++i) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}

int main() {
	freopen("input.txt", "rt", stdin);
	int n;
	int num[100];
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &num[i]);
	}

	PrintArray(num, n);
	int cnt = 0;
	for (int i = 0; i < n - 1; ++i) {
		for (int j = i + 1; j < n; ++j) {
			if (num[j] < 0) {
				Swap(&num[j], &num[i]);
				++cnt;
				break;
			}
		}
	}

	PrintArray(num, n);

	for (int i = 0; i < cnt - 1; ++i)
		for (int j = 0; j < cnt - i - 1; ++j) {
			if (num[j] < num[j + 1])
				Swap(&num[j], &num[j + 1]);
		}


	for (int i = 0; i < n - 1; ++i) {
		for (int j = cnt; j < n - i - 1; ++j) {
			if (num[j] > num[j + 1])
				Swap(&num[j], &num[j + 1]);
		}
	}

	PrintArray(num, n);



	return 0;
}

//
//////34 버블정렬
////void Swap(int* a, int* b) {
////	int temp = *a;
////	*a = *b;
////	*b = temp;
////}
////
////#include <stdio.h>
////int main() {
////	int n;
////	scanf("%d", &n);
////	int num[100];
////	for (int i = 0; i < n; ++i) {
////		scanf("%d", &num[i]);
////	}
////
////	for (int i = 0; i < n-1; ++i) {
////		for (int j = 0; j < n-i-1; ++j) {
////			if (num[j] > num[j + 1]) {
////				Swap(&num[j], &num[j + 1]);
////			}
////
////		}
////	}
////
////
////	return 0;
////}
//
//////34 버블정렬
////void Swap(int* a, int* b) {
////	int temp = *a;
////	*a = *b;
////	*b = temp;
////}
////
////#include <stdio.h>
////int main() {
////	int T;
////	scanf("%d", &T);
////	int num[100];
////	for (int i = 0; i < T; ++i) {
////		scanf("%d", &num[i]);
////	}
////	for (int i = T - 1; i > 0; --i) {
////		for (int j = 0; j < i; ++j) {
////			if (num[j] > num[j + 1]) {
////				Swap(&num[j], &num[j + 1]);
////			}
////
////		}
////	}
////
////
////	return 0;
////}