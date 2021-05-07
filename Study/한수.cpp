//https://www.acmicpc.net/problem/1065

#include <stdio.h>

int main() {
	//freopen("input.txt", "rt", stdin);
	int x,cnt=0, hundred,ten,one;
	scanf("%d", &x);

	if (x < 100) {
		printf("%d", x);
	}
	else {
		for (int i = 100; i <= x; ++i) {
			hundred = i / 100;
			ten = (i % 100)/10;
			one = (i % 100) % 10;
			if (hundred - ten == ten - one)
				++cnt;
		}
		printf("%d", 99+cnt);
	}


	return 0;
}