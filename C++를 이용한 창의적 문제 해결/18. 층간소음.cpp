////18. 층간소음
//#include<stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	
//	int n, m, maxSc = -1, sc = 0;
//	int num;
//	
//	scanf("%d %d", &n, &m);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &num);
//		
//		//기준 값보다 크면 초 값 증가
//		if (num > m)
//			++sc;
//		else {
//			sc = 0;
//		}
//		//다음 번 값에서 기준값을 넘지 않아 sc가 0으로 초기화 되기전 max값에 저장
//		if (maxSc < sc) {
//			maxSc = sc;
//		}
//	}
//
//	//한번도 울리지 않았다면 sc가 증가 하지 않고 sc =0값이 maxSc에도 저장 되었을것
//	if (maxSc == 0) printf("%d", -1);
//	else printf("%d", maxSc);
//
//	return 0;
//
//}


////18. 층간소음
//#include<stdio.h>
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int n, m, maxSc = 0, sc = 0;
//	int num[100] = {0};
//	scanf("%d %d", &n, &m);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &num[i]);
//	}
//	
//
//	for (int i = 0; i < n; ++i) {
//		//기준 값보다 크면 초 값 증가
//		if (num[i] > m) 
//			++sc;
//		else {
//			//초기화 전에 sc값 최대sc랑 비교하고 저장
//			if (maxSc < sc)
//				maxSc = sc;
//			sc = 0;
//		}
//		//else에서 sc 초기화 전에만 max 저장하면 마지막 숫자까지 연속적일 경우 max값 저장 비교할일 없기 때문
//		if (maxSc < sc)
//			maxSc = sc;
//	}
//
//	printf("%d", maxSc);
//	return 0;
//
//}