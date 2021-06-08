//6.숫자만 추출
#include <stdio.h>

int main() {
	//freopen("input.txt", "rt", stdin);
	char str[51];
	scanf("%s", str);
	int res = 0;
	int cnt = 0;
	for (int i = 0; str[i]; ++i) {
		if (str[i] >= 48 && str[i] <= 57) {
			res = res * 10 + (str[i] - 48);
		}
	}

	for (int i = 1; i * i <= res; ++i) {
		if (i * i == res) {
			++cnt;
			break;
		}
		if (res % i == 0) {
			cnt += 2;
		}
	}


	printf("%d\n%d", res, cnt);
	return 0;
}


////효율성 개선전 코드
// //6.숫자만 추출
// #include <stdio.h>

// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	char str[51];
// 	scanf("%s", str);
// 	int res = 0;
// 	int cnt = 0;
// 	for (int i = 0; str[i]; ++i) {
// 		if (str[i] >= 48 && str[i] <= 57) {
// 			res = res * 10 + (str[i] - 48);
// 		}
// 	}

// 	for (int i = 1; i <= res; ++i) {
// 		if (res % i == 0) {

// 			++cnt;
// 		}
// 	}

// 	printf("%d\n%d", res, cnt);
// 	return 0;
// }

// //6.숫자만 추출
// #include<stdio.h>

// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	char ch[10];
// 	int num = 0;
// 	int ten = 0;
// 	int cnt = 0;
// 	scanf("%s", ch);
// 	for (int i = 0; ch[i]; ++i) {
// 		if (ch[i] >= 48 && ch[i] <= 57) {
// 			num = ((num * 10) + (ch[i] - 48));
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
