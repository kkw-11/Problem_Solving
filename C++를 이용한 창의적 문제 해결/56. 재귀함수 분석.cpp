//56. 재귀함수 분석

#include <stdio.h>

void RecursionNumber(int n) {
	if (n == 0)
		return;

	RecursionNumber(n - 1);

	printf("%d ", n);
}


int main() {
//	freopen("input.txt", "rt", stdin);
	int number;
	scanf("%d", &number);
	RecursionNumber(number);
}