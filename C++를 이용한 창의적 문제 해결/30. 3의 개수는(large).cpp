//30. 3의 개수는?(large)
#include <stdio.h>
int main() {
	freopen("input.txt", "rt", stdin);
	int n, cntThree = 0, cntTotal = 0, digit = 0, i, temp = 1, digitStartnum;
	scanf("%d", &n);
	temp = n;
	//자리수 구하기
	while (temp > 0) {
		++digit;
		temp /= 10;
	}

	digitStartnum = 1;
	if (n >= 10) {
		//구한 자리수 아래까지는 규칙대로 3 구하기
		for (i = 1; i < digit; ++i) {
			if (i < 3) {
				cntThree = cntThree * 9 + digitStartnum;
				cntTotal += cntThree;
				digitStartnum *= 10;
			}
			else {
				cntThree = 2 * (digitStartnum / 10);
				cntThree = cntThree * 9 + digitStartnum;
				cntTotal += cntThree;
				digitStartnum *= 10;
			}
		}

		for (i = digitStartnum; i <= n; ++i) {
			temp = i;
			while (temp > 0) {
				if (temp % 10 == 3) {
					++cntTotal;
				}
				temp /= 10;
			}
		}
	}
	else if (n < 10 && n >= 3) {
		cntTotal = 1;
	}




	printf("%d", cntTotal);

	return 0;
}
