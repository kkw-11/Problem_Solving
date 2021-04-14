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

// //59. 부분집합(MS인터뷰:DFS)

// #include <stdio.h>
// #include <stdlib.h>

// int n, ch[11];


// void dfs(int level) {
// 	if (level == n + 1) {
// 		for (int i = 1; i <= n; ++i) {
// 			if (ch[i] == 1)
// 				printf("%d ", i);
// 		}
// 		printf("\n");

// 		return;
// 	}
// 	else {
// 		ch[level] = 1;
// 		dfs(level + 1);

// 		ch[level] = 0;
// 		dfs(level + 1);
// 	}
// }

// int main() {
// 	freopen("input.txt", "rt", stdin);
// 	scanf("%d", &n);

// 	dfs(1);


// 	return 0;
// }