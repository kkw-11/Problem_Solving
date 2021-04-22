//61. 특정 수 만들기(DFS : MS 인터뷰)
#include <stdio.h>
int n, m, cnt;
int num[10];
int path[10];
void dfs(int depth, int total) {
	if (depth == n) {
		if (total == m)
			++cnt;
		return;
	}
	path[depth] = num[depth];
	dfs(depth + 1, total + num[depth]);
	
	path[depth] = -num[depth];
	dfs(depth + 1, total - num[depth]);

	path[depth] = 0;
	dfs(depth + 1, 0 + total);

}
int main() {
	//freopen("input.txt", "rt", stdin);
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &num[i]);
	}

	dfs(0, 0);
	if (cnt == 0) {
		printf("%d", -1);
	}
	else
		printf("%d", cnt);

	return 0;
}