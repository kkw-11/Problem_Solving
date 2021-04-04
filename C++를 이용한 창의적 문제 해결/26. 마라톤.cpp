//26. 마라톤
#include<stdio.h>
#include<stdlib.h>
int main() {
	int n;
	scanf("%d", &n);
	int* p = (int*)malloc(sizeof(int) * n);
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%d", &p[i]);
	}

	for (int i = 0; i < n; ++i) {
		cnt = 1;
		for (int j = 0; j < i; ++j) {
			if (p[i] <= p[j])
				++cnt;
		}
		printf("%d ", cnt);
	}

	free(p);
}