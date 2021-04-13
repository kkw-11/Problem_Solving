//59. 부분집합(MS인터뷰:DFS)

#include <stdio.h>
#include <stdlib.h>

void dfs(int level, int n, int* pch) {
	if (level == n + 1) {
		for (int i = 0; i < n; ++i) {
			if (pch[i] == 1)
				printf("%d ", i + 1);
		}
		printf("\n");

		return;
	}
	pch[level-1] = 1;
	dfs(level + 1, n, pch);
	
	pch[level-1] = 0;
	dfs(level + 1, n, pch);

}

int main() {
	//freopen("input.txt", "rt", stdin);
	int n;
	scanf("%d", &n);

	int* ch = (int*)calloc(n + 1, sizeof(int));


	dfs(1, n, ch);


	return 0;
}