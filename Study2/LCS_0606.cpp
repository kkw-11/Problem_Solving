//https://www.acmicpc.net/problem/9251
#include <cstdio>
#include <cstdlib>
#include <cstring>

char inputstr1[1001];
char inputstr2[1001];

int Max(int a, int b) {

	return a > b ? a : b;
}

int Subsequence(const char* str1, const char* str2) {

	int row = strlen(str1) + 1;
	int col = strlen(str2) + 1;

	int** arr = new int*[row]; 

	for (int i = 0; i < row; ++i) {
		arr[i] = new int[col];
	}
	
	/////////////////////////////////

	//arr[1][1] = str1[0] == str2[0]
	for (int i = 0; i < row; ++i) {
		for (int j = 0; j < col; ++j) {
			arr[i][j] = 0;
		}
	}
	

	//FISH  2  arr[i][j - 1]
	//FINISH 3 arr[i - 1][j] =3 

	for (int i = 1; i < row; ++i) {
		for (int j = 1; j < col; ++j) {
			if (str1[i-1] == str2[j-1])
				arr[i][j] = arr[i - 1][j - 1] + 1;
			else
				arr[i][j] = Max(arr[i - 1][j], arr[i][j - 1]);
		}
	}

	//PrintArray(arr, row, col);
	int retValue = arr[row - 1][col - 1];
	/////////////////////////////////

	for (int i = 0; i < row; ++i) {
		delete[] arr[i];
	}
	delete[] arr;

	return retValue;
}
int main() {
	scanf("%s %s", inputstr1, inputstr2);

	printf("%d\n", Subsequence(inputstr1, inputstr2));
	

	return 0;
}


// //https://www.acmicpc.net/problem/9251
// #include <cstdio>
// #include <cstdlib>
// #include <cstring>

// char inputstr1[1001];
// char inputstr2[1001];

// // void PrintArray(int** arr, int row, int col) {
// // 	for (int i = 0; i < row; ++i) {
// // 		for (int j = 0; j < col; ++j) {
// // 			printf("%5d", arr[i][j]);
// // 		}
// // 		printf("\n");
// // 	}
// // }

// int Max(int a, int b) {

// 	return a > b ? a : b;
// }
// int Subsequence(const char* str1, const char* str2) {

// 	int row = strlen(str1) + 1;
// 	int col = strlen(str2) + 1;

// 	int** arr = new int*[row];

// 	for (int i = 0; i < row; ++i) {
// 		arr[i] = new int[col];
// 	}
// 	////new 연산자 사용법
// 	//arr[0] = new int[col];
// 	//arr[1] = new int[col];
// 	//arr[2] = new int[col];
// 	//arr[3] = new int[col];
// 	//arr[4] = new int[col];
// 	//arr[5] = new int[col];
// 	//arr[6] = new int[col];

// 	/////////////////////////////////

// 	//arr[1][1] == str1[0] == str2[0]
// 	for (int i = 0; i < row; ++i) {
// 		for (int j = 0; j < col; ++j) {
// 			arr[i][j] = 0;
// 		}
// 	}
	
// 	//FISH  2  arr[i][j - 1]
// 	//FINISH 3 arr[i - 1][j] =3 

// 	for (int i = 1; i < row; ++i) {
// 		for (int j = 1; j < col; ++j) {
// 			if (str1[i-1] == str2[j-1])
// 				arr[i][j] = arr[i - 1][j - 1] + 1;
// 			else
// 				arr[i][j] = Max(arr[i - 1][j], arr[i][j - 1]);
// 		}
// 	}

// 	//PrintArray(arr, row, col);
// 	int retValue = arr[row - 1][col - 1];
// 	/////////////////////////////////

// 	for (int i = 0; i < row; ++i) {
// 		delete[] arr[i];
// 	}
// 	delete[] arr;

// 	return retValue;
// }
// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	scanf("%s %s", inputstr1, inputstr2);

// 	printf("%d\n", Subsequence(inputstr1, inputstr2));
	
// 	//system("pause");

// 	return 0;
// }
