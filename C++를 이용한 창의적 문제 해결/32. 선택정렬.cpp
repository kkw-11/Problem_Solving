//32 선택정렬
#include <stdio.h>
void Swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main() {
	freopen("input.txt", "rt", stdin);

	int num[100] = {0};
	int n, minIdx = 0;
	scanf("%d",&n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &num[i]);
	}
		
	for (int i = 0; i < n - 1; ++i) {
		//최소값 찾기
		minIdx = i;
		for (int j = i + 1; j < n; ++j) {
			if (num[minIdx] > num[j])
				minIdx = j;
		}
		//최소값 교환
		Swap(&num[i],&num[minIdx]);

	}

	for (int i = 0; i < n; ++i) {
		printf("%d ", num[i]);
	}

	return 0;
}
