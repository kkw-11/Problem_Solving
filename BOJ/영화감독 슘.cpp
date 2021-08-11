#include <stdio.h>
int movieSeries = 666, tmp, n, cnt;

int main() {

	scanf("%d", &n);

	while (true) {
		tmp = movieSeries;

		while (tmp) {
			if (tmp % 1000 == 666) {
				++cnt;
				break;
			}
			else
				tmp /= 10;
		}

		if (cnt == n){
			printf("%d", movieSeries);
			break;
		}
		movieSeries += 1;

	}

	return 0;
}