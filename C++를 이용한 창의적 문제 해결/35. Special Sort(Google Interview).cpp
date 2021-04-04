//35. Special Sort(Google Interview)
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
	//freopen("input.txt", "rt", stdin);
	int n;
	int num[100];
	int num2[100];
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &num[i]);
	}

	//PrintArray(num, n);

	for (int i = 0; i < n - 1; ++i){
		for (int j = 0; j < (n - 1) - i; ++j) {
			if (num[j] > 0 && num[j + 1] < 0)
				Swap(&num[j], &num[j + 1]);
		}
	}

	PrintArray(num, n);

	return 0;
}
//
//////35 Special Sort(Google Interview)
////#include <stdio.h>
////
////void Swap(int* a, int* b) {
////	int temp = *a;
////	*a = *b;
////	*b = temp;
////}
////
////void PrintArray(int arr[], int size) {
////	for (int i = 0; i < size; ++i) {
////		printf("%d ", arr[i]);
////	}
////	printf("\n");
////}
////
////int main() {
////	//freopen("input.txt", "rt", stdin);
////	int n;
////	int num[100];
////	int num2[100];
////	scanf("%d", &n);
////
////	for (int i = 0; i < n; ++i) {
////		scanf("%d", &num[i]);
////	}
////
////	//PrintArray(num, n);
////	int cnt = 0;
////	int check = 0;
////	for (int i = 0; i < n; ++i) {
////		for (int j = check; j < n; ++j) {
////			if (num[j] < 0) {
////				num2[i] = num[j];
////				check = j + 1;
////				++cnt;
////				break;
////			}
////		}
////	}
////	int check2 = 0;
////	for (int i = cnt; i < n; ++i) {
////		for (int j = check2; j < n; ++j) {
////			if (num[j] > 0) {
////				num2[i] = num[j];
////				check2 = j + 1;
////				break;
////			}
////		}
////	}
////
////	PrintArray(num2, n);
////
////	
////
////	return 0;
////}