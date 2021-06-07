//6.숫자만 추출
#include<stdio.h>

int main() {
	//freopen("input.txt", "rt", stdin);
	char ch[10];
	int num = 0;
	int ten = 0;
	int cnt = 0;
	scanf("%s", ch);
	for (int i = 0; ch[i]; ++i) {
		if (ch[i] >= 48 && ch[i] <= 57) {
			num = ((num * 10) + (ch[i] - 48));
			++ten;
		}
	}

	int j = num;
	for (int i = 1; i < j; ++i) {
		if (num % i == 0) {
			j = num / i;
			cnt += 2;;
		}
	}
	printf("%d\n", num);
	printf("%d", cnt);


	return 0;
}

// //6.숫자만 추출
// #include<stdio.h>

// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	char ch[60];
// 	int num = 0;
// 	int ten = 0;
// 	int cnt = 0;
// 	scanf("%s", ch);
// 	for (int i = 0; ch[i]; ++i) {
// 		if (ch[i] > 47 && ch[i] < 58) {
// 			num = ((ch[i] - 48) + (num * 10));
// 			++ten;
// 		}
// 	}

// 	int j = num;
// 	for (int i = 1; i < j; ++i) {
// 		if (num % i == 0) {
// 			j = num / i;
// 			cnt += 2;;
// 		}
// 	}
// 	printf("%d\n", num);
// 	printf("%d", cnt);


// 	return 0;
// }
