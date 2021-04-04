#include <stdio.h>
#define MAX_N 100

int num[MAX_N] = { 0 };
int main()
{

	int i, j, mod;
	int sum = 0;
	int n;
	scanf_s("%d", &n);
	j = n;
	for (i = 1; i < j; ++i) {
		mod = n % i;
		if (mod == 0) {
			j = n/i;
			sum += i;
			sum += j;
		}
	}

	printf("=%d", sum-n);
}

//#include <stdio.h>
//#define MAX_N 100
//
//int main()
//{
//	int a, b, sum = 0;
//	scanf("%d %d", &a, &b);
//
//	for (int i = a; i <= b; ++i) {
//		sum += i;
//		if (i != b)
//			printf("%d+", i);
//		else
//			printf("%d=");
//	}
//	printf("%d",sum);
//}