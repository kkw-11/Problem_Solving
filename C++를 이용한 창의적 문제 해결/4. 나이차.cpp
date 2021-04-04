//4.나이차
#include<iostream>
using namespace std;
int main() {
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
	int n, i, a, max = -2147000000, min = 2147000000;
	scanf_s("%d", &n);

	for (i = 1; i <= n; i++) {
		cin >> a;
		if (a > max) max = a;
		if (a < min) min = a;
	}
	cout << max - min;
	return 0;
}

////4. 나이차
//#include <stdio.h>
//#include <stdlib.h>
//int main()
//{
//	int max, min;
//	int T;
//	scanf("%d", &T);
//
//	int* pt = (int*)malloc(sizeof(int) * T);
//
//	for (int i = 0; i < T; ++i) {
//		scanf("%d",pt+i);
//	}
//	max = pt[0];
//	min = pt[0];
//
//	for (int j = 0; j < T; ++j) {
//		if (max < pt[j])
//			max = pt[j];
//		if (min > pt[j])
//			min = pt[j];
//	}
//
//	printf("%d", max - min);
//
//	free(pt);
//
//}