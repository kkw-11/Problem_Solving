// https://www.acmicpc.net/problem/11047

#include <stdio.h>
#include <stdlib.h>
int main() {
	//freopen("input.txt", "rt", stdin);
	int N,K,cnt =0;
	// 주어진 N, K 입력받고
	scanf("%d", &N);
	scanf("%d", &K);

	//입력받은 N의 크기만큼 동적배열 할당하고
	int* money = (int*)malloc(sizeof(int) * N);
	//금액 입력받고
	for (int i = 0; i < N; ++i) {
		scanf("%d", &money[i]);
	}

	int j = N - 1;
	//코드 1에서 여러번 뺀 것을 나누기로 몇 뻔뺄수 있는지 한버에 계산하여 시간복잡도 줄임
	while (K > 0) {
		while (K >= money[j]) {
			//cnt += K/money[j];
			cnt = cnt + K/money[j];
			//K %= money[j];
			K = K % money[j];
		}
		--j;
	}

	printf("%d", cnt);
	return 0;
}


//
//
#include <stdio.h>
#include <stdlib.h>
int main() {
//	freopen("input.txt", "rt", stdin);
	int N,K,cnt =0;
	// 주어진 N, K 입력받고
	scanf("%d", &N);
	scanf("%d", &K);

	//입력받은 N의 크기만큼 동적배열 할당하고
	int* money = (int*)malloc(sizeof(int) * N);
	//금액 입력받고
	for (int i = 0; i < N; ++i) {
		scanf("%d", &money[i]);
	}



	int j = N - 1;
	while (K > 0) {
		while (K >= money[j]) {
			K -= money[j];
			++cnt;
		}
		--j;
	}

	printf("%d", cnt);
	return 0;
}