////19. 분노유발자
//#include<stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//
//	int n;
//	int num[100], peonum = 0, max = 0;
//	scanf("%d", &n);
//
//	//읽으면서 처리가 안되기 때문 배열에 저장
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &num[i]);
//	}
//	
//	//마지막 사람부터 검사할예정
//	//처음에는 마지막 혼자이므로 마지막이 최대값
//	//앞으로 검사해가면서 max보다 큰 값 찾으면 그 값이 뒷부분에서 최대값 임 
//	//지금까지의 분노유발자
//	max = num[n - 1];
//
//	for (int i = n-1; i >= 0; --i) {
//		//
//		if (num[i] > max) {
//			++peonum;
//			max = num[i];
//		}
//	}
//
//	printf("%d",peonum);
//
//	return 0;
//
//}
//
////19. 분노유발자
//#include<stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	
//	int n;
//	int num[100], peonum = 0, sum=0;
//	scanf("%d", &n);
//	//읽으면서 처리가 안되기 때문 배열에 저장
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &num[i]);
//	}
//
//	for (int i = 0; i < n-1; ++i) {
//		peonum = 0;
//		for (int j = i + 1; j < n; ++j) {
//
//			//기준학생보다 작은 학생수 카운트
//			if (num[i] > num[j])
//				peonum += 1;
//		}
//
//		//뒷 학생수가 모두 기준 학생보다 작을 경우 분노유발자
//		//첫번째 학생: 기분보다 n-1명 작으면 분노유발자
//		//두번째 학생: 기분보다 n-2명 작으면 분노유발자
//		if (peonum == n - 1 - i) sum +=1;
//			
//	}
//
//	printf("%d", sum);
//
//	return 0;
//
//}
//
//
////19. 분노유발자
//#include<stdio.h>
//int main() {
//	freopen("input.txt", "rt", stdin);
//	int n;
//	int num[100], sum = 0;
//	scanf("%d", &n);
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &num[i]);
//	}
//
//	for (int i = 0; i < n-1; ++i) {
//		int j;
//		for ( j = i + 1; j < n; ++j) {
//			//기준학생보다 큰 학생 있다면 분노유발자 아님 검사 종료
//			//다음기준학생 검사
//			if (num[i] <= num[j]) {
//				break;
//			}		
//		}
//// 끝까지 갔으면 모두 기준학생보다 작은 것 
////분노유발자 한명 추가
//		if (j == n)
//			sum += 1;
//	}
//	printf("%d", sum);
//
//	return 0;
//
//}