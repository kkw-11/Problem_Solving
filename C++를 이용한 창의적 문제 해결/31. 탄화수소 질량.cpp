//31. 탄화수소 질량 
// 코드수정(by 가독성)
#include <stdio.h>
int main() {
	//freopen("input.txt", "rt", stdin);
	char ch[100];
	int summass = 0, sumc = 0, sumh = 0, carbon = 0, hydrogen = 0;
	scanf("%s", ch);
	int i, pos;

	//pos로 H의 위치 표시
	if (ch[1] == 'H') {
		sumc = 1;
		pos = 1;
	}
	else {
		//H가 나올 때까지 탄소의 수를 구함
		for (i = 1; ch[i] != 'H'; ++i) {
			sumc = sumc * 10 + (ch[i] - 48);
		}
		pos = i;
	}

	//H 문자 다음 부터 수소의 수를 구함
	//이때 H다음에 1일 경우는 예외로 따로 구해준다.
	if (ch[pos + 1] == '\0')
		sumh = 1;
	else {
		for (i = pos + 1; ch[i] != '\0'; ++i) {
			sumh = sumh * 10 + (ch[i] - 48);
		}
	}
//
//
//	summass = sumc * 12 + sumh;
//
//	printf("%d", summass);
//	return 0;
//}


////31. 탄화수소 질량
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	char ch[100];
//	int summass = 0, sumc = 0, sumh = 0, carbon = 0, hydrogen = 0;
//	scanf("%s", ch);
//	int i, j;
//
//	//i로 H의 위치 표시
//	if (ch[1] == 'H') {
//		i = 1;
//		sumc = 1;
//	}
//	else {
//		//H가 나올 때까지 탄소의 수를 구함
//		for (i = 1; ch[i] != 'H'; ++i) {
//			carbon = ch[i] - 48;
//			sumc = sumc * 10 + carbon;
//		}
//	}
//
//	//H 문자 다음 부터 수소의 수를 구함
//	//이때 H다음에 1일 경우는 예외로 따로 구해준다.
//	if (ch[i + 1] == '\0')
//		sumh = 1;
//	else {
//		for (j = i + 1; ch[j] != '\0'; ++j) {
//			hydrogen = ch[j] - 48;
//			sumh = sumh * 10 + hydrogen;
//		}
//	}
//
//
//
//	summass = sumc * 12 + sumh;
//
//	printf("%d", summass);
//	return 0;
//}