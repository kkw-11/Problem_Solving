//9. 모두의 약수
#include <stdio.h>
int main() {

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		int cnt = 0;
		int quotient = i;

		//약수 개수 구하기
		if (i == 1)//1의 약수 개수 무조건 1 // else 조건으로 반복문 실행하면 0 이 출력됨
			printf("%d ", 1);
		else {//2부터 약수 개수 구하기 반복문 횟수 줄이기 위해서 나누는 값으 1부터 n 까지 하지말고 몫 직전까지 
			for (int j = 1; j < quotient; ++j) {
				if (i % j == 0) {
					quotient = i / j;
					if (j == quotient)  
						cnt += 1; // 제곱수의 경우 약수 개수 1개 증가
					else
						cnt += 2; // 제곱 수가 아닌 이상 약수의 개수 2개씩 증가
				}
			}

			printf("%d ", cnt);
		}
	}

	return 0;

}