//13. 가장 많이 사용된 자릿수
#include <stdio.h>
int main() {
	//freopen("input.txt", "rt", stdin);
	char num[100] = { 0 };
	scanf("%s", num);
	int digit[10] = { 0 };
	int mod = 0, max = -1, maxIndex;
	
	for (int i = 0; num[i]; ++i) {
		int check = num[i] - 48;
		++digit[check];
	}

	for (int i = 9; i >= 0; --i) {
		if (max <= digit[i]) {
			max = digit[i];
			maxIndex = i;
		}
	}

	//for (int i = 9; i >= 0; --i) {
	//	if (max == digit[i]) {
	//		maxIndex = i;
	//		break;
	//	}
	//}

	printf("%d", maxIndex);
	return 0;
}

////13. 가장 많이 사용된 자릿수
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	char num[100] = {0};
//	scanf("%s", num);
//	int digit[10] = { 0 };
//	int mod = 0, max = -1, maxIndex;
//
//	for (int i = 0; num[i]; ++i) {
//		int check = num[i] - 48;
//		
//		switch (check)
//		{
//		case 0:
//			++digit[0];
//			break;
//		case 1:
//			++digit[1];
//			break;
//		case 2:
//			++digit[2];
//			break;
//		case 3:
//			++digit[3];
//			break;
//		case 4:
//			++digit[4];
//			break;
//		case 5:
//			++digit[5];
//			break;
//		case 6:
//			++digit[6];
//			break;
//		case 7:
//			++digit[7];
//			break;
//		case 8:
//			++digit[8];
//			break;
//		case 9:
//			++digit[9];
//			break;
//		default:
//			break;
//		}
//	}
//
//	for (int i = 9; i >= 0; --i) {
//		if (max < digit[i])
//			max = digit[i];
//	}
//
//	for (int i = 9; i >= 0; --i) {
//		if (max == digit[i]) {
//			maxIndex = i;
//			break;
//		}
//	}
//	
//	
//	printf("%d", maxIndex);
//	return 0;
//}

////13. 가장 많이 사용된 자릿수
//#include <stdio.h>
//int main() {
//	long long n;
//	scanf("%d",&n);
//	int digit[10] = {0};
//	int mod = 0, max = -1, maxIndex;
//	int temp = n;
//	
//	while (temp) {
//		mod = temp % 10;
//		++digit[mod];
//		temp /= 10;
//	}
//
//	for (int i = 0; i < 10; ++i) {
//		printf("%d ", digit[i]);
//	}
//	printf("\n");
//
//	for (int i = 9; i >= 0; --i) {
//		if (max < digit[i])
//			max = digit[i];
//	}
//
//	for (int i = 9; i >= 0; --i) {
//		if (max == digit[i]) {
//			maxIndex = i;
//			break;
//		}
//	}
//
//	printf("%d", maxIndex);
//
//	return 0;
//}