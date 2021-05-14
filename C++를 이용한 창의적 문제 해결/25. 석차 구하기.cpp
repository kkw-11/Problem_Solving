////25. 석차 구하기
//#include <stdio.h>
//#include <stdlib.h>
//
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, cnt = 0;
//	scanf("%d", &n);
//	int* p1 = (int*)malloc(sizeof(int) * n);
//	int* p2 = (int*)malloc(sizeof(int) * n);
//
//	//점수배열과, 등수표시 배열값 입력
//	//등수표시 배열은 초기값 1로 설정
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &p1[i]);
//		p2[i] = 1;
//	}
//
//
//	for (int i = 0; i < n; ++i) {
//		for (int j = 0; j < n; ++j) {
//			if (p1[i] < p1[j])
//				++p2[i];
//		}
//	}
//
//	for (int i = 0; i < n; ++i) {
//		printf("%d ",p2[i]);
//	}
//	free(p1);
//	free(p2);
//
//	return 0;
//}
//
////25. 석차 구하기
//#include <stdio.h>
//#include <stdlib.h>
//void Swap(int* pa, int* pb) {
//	int temp = *pa;
//	*pa = *pb;
//	*pb = temp;
//}
//void Print(int list[], int size) {
//	for (int i = 0; i < size; ++i) {
//		printf("%5d", list[i]);
//	}
//	printf("\n");
//}
//void _Sort(int list[], int left, int right) {
//
//	if (left <= right) {
//		int pivot = left;
//		int i = left + 1;
//		int j = right;
//
//		do {
//			while (list[pivot] > list[i])
//				++i;
//			while (list[pivot] < list[j])
//				--j;
//
//			if (i <= j) {
//				Swap(&list[i], &list[j]);
//				++i;
//				--j;
//			}
//			Print(list, 5);
//		} while (i <= j);
//
//		Swap(&list[pivot], &list[j]);
//		Print(list, 5);
//
//		_Sort(list, left, j - 1);
//		_Sort(list, j + 1, right);
//
//	}
//
//}
//void Sort(int list[], int size) {
//	_Sort(list, 0, size - 1);
//}
//
//
//int main() {
//	freopen("input.txt", "rt", stdin);
//	int n, cnt = 0;
//	scanf("%d", &n);
//	int* p1 = (int*)malloc(sizeof(int) * n);
//	int* p2 = (int*)malloc(sizeof(int) * n);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &p1[i]);
//		p2[i] = p1[i];
//	}
//	Print(p1, 5);
//	
//	//정렬
//	Sort(p2, n);
//
//
//	//p1 첫 인덱스부터 정렬된 p2의 값을 찾아서 등수 출력
//	for (int i = 0; i < n; ++i) {
//		cnt = 1;
//		for (int j = n - 1; j >= 0; --j) {
//			if (p1[i] == p2[j]) {
//				printf("%d ", cnt);
//				break;
//			}
//			++cnt;
//		}
//	}
//	free(p1);
//	free(p2);
//
//	return 0;
//}
//