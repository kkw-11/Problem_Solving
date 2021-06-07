//8.올바른 괄호
#include <stdio.h>
int main() {
	char ch[100];
	int laststring = 0;
	int cnt = 0;
	scanf("%s", ch);

	for (int i = 0; ch[i]; ++i) {
		laststring = i;
	}

	for (int j = laststring; j >= 0; --j) {
		if (ch[j] == '(')
			--cnt;
		else if (ch[j] == ')')
			++cnt;
		else
			cnt = -1;

		if (cnt < 0)
			break;
	}

	if (cnt == 0)
		printf("YES\n");
	else
		printf("NO\n");
	
	return 0;
}
////8.올바른 괄호 -강의
//#include <stdio.h>
//int main() {
//	char ch[100];
//	int laststring = 0;
//	int cnt = 0;
//	scanf("%s", ch);
//
//	for (int i = 0; ch[i]; ++i) {
//		if (ch[i] == '(')
//			++cnt;
//		else if (ch[i] == ')')
//			--cnt;
//		else
//			cnt = -1;
//
//		if (cnt < 0)
//			break;
//	}
//
//	if (cnt == 0)
//		printf("YES\n");
//	else
//		printf("NO\n");
//
//	return 0;
//}
