//////36. 삽입정렬
////#include <stdio.h>
////
////void PrintArray(int arr[], int size) {
////	for (int i = 0; i < size; ++i) {
////		printf("%d ", arr[i]);
////	}
////	printf("\n");
////}
////
////int main() {
////	freopen("input.txt", "rt", stdin);
////	int n;
////	int num[100];
////	scanf("%d", &n);
////
////	for (int i = 0; i < n; ++i) {
////		scanf("%d", &num[i]);
////	}
////
////	PrintArray(num, n);
////
////	int value;
////	int j;
////	for (int i = 1; i < n; ++i) {
////		value = num[i];
////		for (j = i - 1; j >= 0; --j) {
////			if (num[j] > value) {
////				num[j + 1] = num[j];
////			}
////			else {
////				break;
////			}
////		}
////		num[j + 1] = value;
////	}
////	PrintArray(num, n);
////
////
////	return 0;
////}