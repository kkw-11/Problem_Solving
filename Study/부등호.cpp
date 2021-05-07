#include<stdio.h>
#include<string.h>

void swap(int a, int b);
void bf(int flag, int n);
int check();

char str[11], max[11], min[11], copy[11];

int main() {
	int k, i;
	scanf("%d", &k);
	for (i = 0; i <= k; i++) {
		if (i != k) {
			getchar();
			str[i] = getchar();
		}
		else str[i] = NULL;
        //부등호의 수 + 1만큼의 수를 
        //최대 값에서는 9부터 아래로 하나씩 입력
        //최소 값에서는 0부터 위로 하나씩 입력
		max[i] = '9' - k + i;
		min[i] = '0' + k - i;
	}
	max[i] = NULL;
	min[i] = NULL;
	strcpy(copy, max);
	bf(1, k + 1);
	strcpy(copy, min);
	bf(0, k + 1);
	printf("%s\n%s", max, min);
    	return 0;
}

void swap(int a, int b) {
	char tmp;
	tmp = copy[a];
	copy[a] = copy[b];
	copy[b] = tmp;
}
//flag 1이면 최대값 구하기
//flag 0이면 최소값 구하기
void bf(int flag, int n) {
	if (n == 1) {
        //부등호 값에 이상이 없이 숫자 배열이 되었다면 최대 최소 비교
		if (check()) {
			if (flag) {
                //strcmp 문자열 비교 함수 
                //strcmp(str1, str2);  
                //str1 < str2 인 경우에는 음수 반환
				if (strcmp(max, copy) < 0) {
					strcpy(max, copy);
				}
			}
			else {
                //str1 > str2 인 경우에는 양수 반환
				if (strcmp(min, copy) > 0) {
					strcpy(min, copy);
				}
			}
		}
	}
    //모든 경우의 수 배열하기
    //순열 짜기 기본 코드
	for (int i = 0; i < n; i++) {
		swap(i, n - 1);
		bf(flag, n - 1);
		swap(i, n - 1); //다시 원래 위치로 되돌리기
	}
}
int check() {
	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == '<') {
			if (copy[i] >= copy[i + 1]) {
				return 0;
			}
		}
		else if(str[i] == '>'){
			if (copy[i] <= copy[i + 1]) {
				return 0;
			}
		}
	}
	return 1;
}


//https://ggodong.tistory.com/138 순열 구현하기
// #include <stdio.h>

// int arr[4] = { 1, 2, 3, 4 };
// int len = 4;

// void swap(int a, int b) {
// 	int temp = arr[a];
// 	arr[a] = arr[b];
// 	arr[b] = temp;
// }

// void permu(int N) {
// 	if (N == 3) {
// 		for (int i = 0; i < 4; i++) {
// 			printf("%d", arr[i]);
// 		}
// 		printf("\n");
// 	}
// 	else {
// 		for (int i = N; i < 4; i++) {
// 			swap(i, N);
// 			permu(N + 1);
// 			swap(i, N);
// 		}
// 	}
// }

// int main(void) {
// 	permu(0);
// }