//60. 합이 같은 부분집합(DFS : 아마존 인터뷰)
#include <stdio.h>
#include <stdlib.h>
int n;
bool flag = 0;
int num[10];
int subnum[10];
int sum1;
int sum2;
//부분집합 구하기
void dfs(int level) {
	if (flag == true) return;
	if (level == n) {

		//부분집합 누적합 구하기
		sum1 = sum2 = 0;
		for (int i = 0; i < n; ++i) {
			if (subnum[i] == true) {
				sum1 += num[i];
			}
			else {
				sum2 += num[i];
			}
		}

		if (sum1 == sum2) {
			flag = 1;
		}
		return;
	}

	subnum[level] = true;
	dfs(level + 1);

	subnum[level] = false;
	dfs(level + 1);

}

int main() {
	//freopen("input.txt", "rt", stdin);
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &num[i]);
	}
	//부분집합 구하기
	dfs(0);

	if (flag == 1) {
		printf("YES\n");
		return 0;
	}

	printf("NO\n");
	return 0;
}

////60. 합이 같은 부분집합(DFS : 아마존 인터뷰)
//#include<stdio.h>
//int n,total;
//int flag = 0;
//int num[10];
//
//void dfs(int depth, int sum) {
//  if(sum>(total/2)) return;
//	if (flag == 1) return;
//	//모든 원소에 대해서 부분집합에 포함시킬지 말지 결정했을때(depth == n)
//	//부분집합의 합에 대해서 나머지 부분집합과 비교할 차례
//
//	if (depth == n) {
//		if (sum == total - sum)
//			flag = 1;
//
//
//		return;
//
//	}
//	else {
//		
//		dfs(depth + 1, sum + num[depth]);
//
//		dfs(depth + 1, sum );
//
//	}
//
//}
//
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	scanf("%d", &n);
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &num[i]);
//		total += num[i];
//	}
//
//	dfs(0,0);
//
//	if (flag == 1)
//		printf("YES");
//	else
//		printf("NO");
//
//
//	return 0;
//}
