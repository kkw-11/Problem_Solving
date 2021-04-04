//3. 진약수
#include <stdio.h>
#define MAX_N 100

int num[MAX_N] = { 0 };
int main()
{

	int i, j, mod;
	int sum = 0;
	int n;
	scanf_s("%d", &n);
	j = 0;
	for (i = 1; i < n; ++i) {
		if (n % i == 0){
			sum += i;
			num[j] = i;
			++j;
		}
	}
	--j;
	for (int k = 0; k <= j; ++k)
		if (k == j)
			printf("%d=", num[k]);
		else
			printf("%d+", num[k]);

	printf("%d", sum);
}