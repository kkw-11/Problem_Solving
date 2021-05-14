///21. 카드 게임
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int cardA[10], cardB[10], res[10];
//	int scoreA = 0, scoreB = 0;
//	int lw = 0;
//	for (int i = 0; i < 10; ++i) {
//		scanf("%d", &cardA[i]);
//	}
//	for (int i = 0; i < 10; ++i) {
//		scanf("%d", &cardB[i]);
//	}
//
//	for (int i = 0; i < 10; ++i) {
//		if (cardA[i] > cardB[i]) {
//			lw = 'A';
//			scoreA += 3;
//		}
//
//		else if (cardA[i] < cardB[i]) {
//			lw = 'B';
//			scoreB += 3;
//		}
//		else {
//			scoreA += 1;
//			scoreB += 1;
//		}
//	}
//
//	printf("%d %d\n", scoreA, scoreB);
//	if (scoreA == scoreB) {
//		if (lw == 0)
//			printf("D\n");
//		else
//			printf("%c", lw);
//
//	}
//	else if (scoreA > scoreB) printf("A\n");
//	else printf("B\n");
//
//
//	return 0;
//}
//
////21. 카드 게임
//#include <stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int cardA[10], cardB[10], res[10];
//	int scoreA = 0, scoreB = 0;
//
//	for (int i= 0; i < 10; ++i) {
//		scanf("%d", &cardA[i]);
//	}
//	for (int i = 0; i < 10; ++i) {
//		scanf("%d", &cardB[i]);
//	}
//
//	for (int i = 0; i < 10; ++i) {
//		if (cardA[i] > cardB[i]) {
//			res[i] = 'A';
//			scoreA += 3;
//		}
//		else if (cardA[i] < cardB[i]) {
//			res[i] = 'B';
//			scoreB += 3;
//		}			
//		else {
//			res[i] = 'D';
//			scoreA += 1;
//			scoreB += 1;
//		}
//	}
//
//	printf("%d %d\n", scoreA, scoreB);
//	if (scoreA == scoreB) {
//		int j = 0;
//		for (j = 9; j >= 0; --j) {
//			if (res[j] == 'A' || res[j] == 'B') {
//				printf("%c", res[j]);
//				break;
//			}
//		}
//		if (j == -1)
//			printf("D\n");
//
//	}
//	else if (scoreA > scoreB) printf("A\n");
//	else printf("B\n");
//
//	return 0;
//}