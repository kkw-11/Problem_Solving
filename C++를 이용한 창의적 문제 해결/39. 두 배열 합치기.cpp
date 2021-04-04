//39. 두 배열 합치기
#include<stdio.h>
int main() {
	//freopen("input.txt", "rt", stdin);
	int N, M;
	int a[100] = { 0 }, b[100] = { 0 }, c[200];
	scanf("%d", &N);

	for (int i = 0; i < N; ++i) {
		scanf("%d", &a[i]);
	}

	scanf("%d", &M);

	for (int i = 0; i < M; ++i) {
		scanf("%d", &b[i]);
	}

	int i = 0, j = 0, k = 0;

	while (i < N && j < M) {

		if (a[i] <= b[j])
			c[k++] = a[i++];
		else
			c[k++] = b[j++];

	}
	//i>=N Or j>=M 이면 위의 조건문을 빠져나간다.
	//이때 j<M이면 b배열의 남은 값을 c에 넣고
	//j<N이면 a배열의 남은 값을 c에 넣는다.

	//while문이 순서대로 2개 존재하지만 두개의 while문은 모두 실행되지 않는다.
	while (i >= N && j < M) {
		c[k++] = b[j++];
	}

	while (i < N && j >= M) {
		c[k++] = a[i++];
	}
	for (int i = 0; i < N + M; ++i) {
		printf("%d ",c[i]);
	}

}