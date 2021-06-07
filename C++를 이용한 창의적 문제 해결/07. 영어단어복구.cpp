

//7.영어단어복구-강의풀이
#include <stdio.h>
int main() {
	//freopen("input.txt", "rt", stdin);
	char str[101], restr[101];

	gets_s(str);
	int j = 0;
	for (int i = 0; str[i]; ++i) {
		if (str[i] != ' ') {
			if (str[i] >= 65 && str[i] <= 90)//A: 65, Z: 90
				restr[j++] = str[i] + 32; //후위 증감 대입하고 j는 1 증가
			else
				restr[j++] = str[i]; 
		}
	}
	restr[j] = '\0'; //문자열 마지막에 널 문자 입력으로 %s로 출력하기 위해
	printf("%s",restr);

	return 0;
}

////7.영어단어복구
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	char str[101];
//	gets_s(str);
//
//	for (int i = 0; str[i]; ++i) {
//		if (str[i] >= 65 && str[i] <= 122) {
//			{
//				if (str[i] >= 65 && str[i] <= 90) {
//					str[i] = str[i] + 32;
//				}
//				printf("%c", str[i]);
//			}
//		}
//	}	
//
//	return 0;
//}