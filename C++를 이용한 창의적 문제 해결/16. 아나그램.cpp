////16.아나그램
//#include <stdio.h>
//void Swap(char* pa, char* pb) {
//	char temp = *pa;
//	*pa = *pb;
//	*pb = temp;
//}
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	char ch1[200], ch2[200];
//	int flag = 0;
//
//	//문자입력받기
//	scanf("%s", ch1);
//	scanf("%s", ch2);
//
//	/*
//	첫번째 문자의 첫번째 인덱스부터 다음문자에 있는지 점검 있으면 교체
//	첫 번째 문자의 다음 인덱스 점검
//	위 상황 반복
//	매번 마다 flag 변수로 교체 상황 체크
//	교체가 없이 끝났다면 같은 문자 더이상 없으므로 아나그램 아님 루프문 종료
//	*/
//	for (int i = 0; ch1[i]; ++i) {
//		flag = 0;
//		for (int j = i; ch2[j]; ++j) {
//			if (ch1[i] == ch2[j]) {
//				Swap(&ch2[i], &ch2[j]);
//				flag = 1;
//				break;
//			}
//		}
//		//같은것 있으면 교체했음 체크
//		//flag 그대로 0이면 같은것 없음 교체 안했음
//		if (flag == 0)break;
//	}
//
//	if (flag == 0) printf("NO");
//	else printf("YES");
//	
//	return 0;
//}
//
////16.아나그램
//#include <stdio.h>
//void _Sort(char list[], int left, int right) {
//	if (left <= right) {
//		int pivot = left;
//		int i = left + 1;
//		int j = right;
//		do {
//
//			while (list[pivot] > list[i])
//				++i;
//			while (list[pivot] < list[j])
//				--j;
//			if (i <= j) {
//				//swap
//				int temp = list[i];
//				list[i] = list[j];
//				list[j] = temp;
//		
//				++i;
//				--j;
//			}
//		} while (i <= j);
//
//		int temp = list[j];
//		list[j] = list[pivot];
//		list[pivot] = temp;
//
//		_Sort(list, left, j - 1);
//		_Sort(list, j + 1, right);
//
//
//	}
//}
//void Sort(char list[], int size) {
//	_Sort(list, 0, size - 1);
//}
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	char ch1[100], ch2[200];
//	int size;
//
//	//문자입력받기
//	scanf("%s", ch1);
//	scanf("%s", ch2);
//
//	//마지막 null값으로 사이즈 구하기
//	int i = 0;
//	for (i = 0; ch1[i]; ++i) {
//	}
//
//	size = i;
//
//	//정렬
//	Sort(ch1, size);
//	Sort(ch2, size);
//
//	//인덱스별로 비교하기
//	//비교하다가 하나라도 다르면 NO 출력
//	int j;
//	for (j = 0; ch1[j]; ++j) {
//		if (ch1[j] != ch2[j]) {
//			printf("NO");
//			break;
//		}
//	}
//	
//	//i값이 null과 같으면 YES출력
//	if (j == size)
//		printf("YES");
//
//
//	return 0;
//}