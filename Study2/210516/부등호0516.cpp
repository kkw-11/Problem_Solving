#include <stdio.h>
int main() {
	
	
	//freopen("input.txt", "rt", stdin);
	int k, i =0,cnt = 0;
	char curMax = '9', curMin = '0';
	char str[11],max[11],min[11];
	scanf("%d", &k);

	for (int i = 0; i < k; ++i) {
		scanf(" %c", &str[i]);
	}

	//부등호의 개수는 k개 
	//마지막 부등호배열의 인덱스 번호는 k-1
	//마지막 숫자의 인덱스 번호는 k
	//마지막 숫자 까지 입력하고 인덱스 i가 k+1이 되면 while문 종료
	while (i != k+1) {
		if (str[i] == '>') {
			max[i++] = curMax--;
		}
		else if (str[i] == '<') {
			for (int j = i; str[j] == '<'; ++j) {
				++cnt;
			}
			//cnt를 가지고 그 다음 최대숫자를 구할 수 있는데 cnt가 변경되기 때문에 temp에 저장해둠
			int temp = cnt;
			for (; cnt >= 0; --cnt) {
				max[i++] = curMax - cnt;
			}
			cnt = 0;
			curMax -= ++temp;
		}
		else //'>' 다음 str[i]가 널이라면 max[i]에 현재 최대값 넣고 종료
			max[i++] = curMax;

	}
	max[i] = NULL;

	i = 0;
	while (i != k+1) {
		if (str[i] == '<') {
			min[i++] = curMin++;
		}
		else if (str[i] == '>') {
			for (int j = i; str[j] == '>'; ++j) {
				++cnt;
			}
			int temp = cnt;
			for (; cnt >= 0; --cnt) {
				min[i++] = curMin + cnt;
			}
			cnt = 0;
			curMin += ++temp;
		}
		else //'>' 다음 str[i]가 널이라면 min[i]에 현재 최소값넣고 종료
			min[i++] = curMin;
	}

	min[i] = NULL;
	printf("%s\n%s",max,min);
	return 0;
}


// #include <stdio.h>
// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	int k, i =0,cnt = 0;
// 	char curMax = '9', curMin = '0';
// 	char str[11],max[11],min[11];
// 	scanf("%d", &k);

// 	for (int i = 0; i < k; ++i) {
// 		scanf(" %c", &str[i]);
// 	}

// 	while (i != k+1) {
// 		if (str[i] == '>') {
// 			max[i++] = curMax--;
// 		}
// 		else if (str[i] == '<') {
// 			for (int j = i; str[j] == '<'; ++j) {
// 				++cnt;
// 			}
// 			int temp = cnt;
// 			for (; cnt >= 0; --cnt) {
// 				max[i++] = curMax - cnt;
// 			}
// 			cnt = 0;
// 			curMax -= ++temp;
// 		}
// 		else
// 			max[i++] = curMax;

// 	}
// 	max[i] = NULL;

// 	i = 0;
// 	while (i != k+1) {
// 		if (str[i] == '<') {
// 			min[i++] = curMin++;
// 		}
// 		else if (str[i] == '>') {
// 			for (int j = i; str[j] == '>'; ++j) {
// 				++cnt;
// 			}
// 			int temp = cnt;
// 			for (; cnt >= 0; --cnt) {
// 				min[i++] = curMin + cnt;
// 			}
// 			cnt = 0;
// 			curMin += ++temp;
// 		}
// 		else
// 			min[i++] = curMin;
	
// 	}

// 	min[i] = NULL;
// 	printf("%s\n%s",max,min);
// 	return 0;
// }


// //https://www.acmicpc.net/problem/2529
// #include <stdio.h>

// int main()
// {
// 	int max[10], min[10], k, cur_max=9, cur_min=0;
// 	char sign[12];

// 	scanf("%d", &k);
// 	for (int i = 0; i < k; i++)
// 		scanf(" %c", &sign[i]);

// 	int i = 0, count=0, sub=0;  
// 	// count: 현재 위치에서 '<'가 몇개 나오는지 개수
// 	// sub: '<'가 처음 나오는 위치에서 count 값. count 값이 변화하기 때문에 새 변수로 저장. '<'가 끝나는 순간 cur_max에서 빼주기 위해 설정. 

// 	while (1)
// 	{
// 		if (sign[i] == '>')
// 		{
// 			max[i] = cur_max--;
// 			if (sub)
// 			{
// 				cur_max -= sub;
// 				sub = 0;
// 			}
// 		}
// 		else if(sign[i]=='<')
// 		{
// 			if (count == 0)
// 			{
// 				int j = i;
// 				while (sign[j] == '<')
// 				{
// 					j++;
// 					count++;
// 				}
				
// 				sub = count;
// 				max[i] = cur_max - count;
// 				count--;
// 			}
// 			else
// 			{
// 				max[i] = cur_max - count;
// 				count--;
// 			}
			
// 		}
// 		else
// 		{
// 			max[i] = cur_max;
// 			break;
// 		}
// 		i++;
// 	}

// 	for (int i = 0; i <= k; i++)
// 		printf("%d", max[i]);
// 	printf("\n");

// 	int add=0;
// 	i = 0, count=0;
// 	while (1)
// 	{
// 		if (sign[i] == '<')
// 		{
// 			min[i] = cur_min++;
// 			if (add)
// 			{
// 				cur_min += add;
// 				add = 0;
// 			}
// 		}
// 		else if (sign[i] == '>')
// 		{
// 			if (count == 0)
// 			{
// 				int j = i;
// 				while (sign[j] == '>')
// 				{
// 					j++;
// 					count++;
// 				}
// 				add = count;
// 				min[i] = cur_min + count;
// 				count--;
// 			}
// 			else
// 			{
// 				min[i] = cur_min + count;
// 				count--;
// 			}

// 		}
// 		else
// 		{
// 			min[i] = cur_min;
// 			break;
// 		}
// 		i++;
// 	}
// 	for (int i = 0; i <= k; i++)
// 		printf("%d", min[i]);
// 	return 0;
// }

// // //https://www.acmicpc.net/problem/2529
// #include<stdio.h>
// #include<string.h>

// void swap(int a, int b);
// void permu(int flag, int start, int end); // 9 8 7 => 6가지 978 897 879 798 789
// int check();
// void checkfindMaxMin(int flag);

// char str[11], max[11], min[11], copy[11];
// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	int k, i;
// 	scanf("%d", &k);
// 	//부등호의 개수가 k면 숫자는 k+1
// 	//부등호 저장 배열의 마지막 인덱스는 k-1
// 	//부등호 사이에 들어갈 수의 개수는 k
// 	for (i = 0; i <= k; i++) {
// 		if (i != k) {
// 			getchar();
// 			str[i] = getchar();
// 		}
// 		else str[i] = NULL;
// 		//부등호의 수 + 1만큼의 수를 
// 		//최대 값에서는 9-k부터 9까지 하나씩 입력
// 		//최소 값에서는 0+k부터 하나씩 입력
// 		//max에는 입력가능한 수들 중에 가장 작은값을 초기값으로 넣어주고
// 		max[i] = '9' - k + i; 
// 		//min에는 입력가능한 수들 중에 가장 큰값을 초기 값으로 넣어주고
// 		min[i] = '0' + k - i; 
// 	}
// 	max[i] = NULL;
// 	min[i] = NULL;

// 	//알고리즘은 max와 min이 아닌 copy값으로 수행 하기위해 복사본 저장
// 	strcpy(copy, max);
// 	//flag=1, 최대값 구하기
// 	permu(1, 0, k);

// 	strcpy(copy, min);
// 	//flag=0, 최소값 구하기
// 	permu(0, 0, k);

// 	printf("%s\n%s", max, min);
// 	return 0;
// }

// void swap(int a, int b) {
// 	char tmp;
// 	tmp = copy[a];
// 	copy[a] = copy[b];
// 	copy[b] = tmp;
// }

// //flag 1이면 최대값 구하기
// //flag 0이면 최소값 구하기
// //7,8,9
// void permu(int flag, int start, int end) {
// 	//start가 숫자 배열의 범위를 벗어났을 경우 이제 모두 정렬한 상태
// 	//정렬한 상태에서 부등호와 맞는지 체크하고 맞다면 현재값이 최대값과 비교하여 최대값 구하기
// 	if (start == end + 1) {
// 		checkfindMaxMin(flag);
// 	}

// 	//모든 경우의 수 배열하기
// 	//순열 알고리즘 기본 코드
// 	//i가 main에서 넘겨준 start부터 end 까지 변할때 i마다 DFS를 수행하며 순열구하기
// 	//반복문for문의 i가 변하면서 DFS의 시작점이 변함
// 	//제일 왼쪽을 기준으로 DFS로 모든 경우 배열해보고 다시 ++i로 다음 인덱스를 기준으로 DFS로 모든 경우 배열해보고 반복 ...
// 	/*
// 	처음 호출된 permu 함수 (즉, 메모리의 가장 아래 스택에서) 기준으로만 생각해서 for문을 보면 start 값은 계속 0이고 i만 증가하면서 
// 	swap을 하는 것은 첫 번째 올 문자를 정해준다고 생각하면 됨 
// 	수형도를 그려 직접 손으로 순열을 직접 다 구할때 각 문자에 대해 첫 번째 오는 경우를 적어두고 다음 경우들을 적어두면서 하는 것처럼 
// 	생각하면 됨
// 	*/
// 	//7,8,9  8,7,9   9,8,7 
// 	for (int i = start; i <= end; i++) {
// 		swap(start, i);
// 		permu(flag, start + 1, end);
// 		swap(start, i); //각 스택마다 배열의 위치를 함수호출 직전으로 되돌리기
// 	}
// }

// void checkfindMaxMin(int flag) {
// 	//부등호 값에 이상이 없이 숫자 배열이 되었다면 최대 최소 비교
// 	if (check()) {
// 		//flag 1 최대값 체크, flat 0 최소값 체크
// 		if (flag) {
// 			//strcmp 문자열 비교 함수 
// 			//strcmp(str1, str2);  
// 			//str1 < str2 인 경우에는 음수 반환
// 			if (strcmp(max, copy) < 0) {
// 				strcpy(max, copy);
// 			}
// 		}
// 		else {
// 			//str1 > str2 인 경우에는 양수 반환
// 			if (strcmp(min, copy) > 0) {
// 				strcpy(min, copy);
// 			}
// 		}
// 	}
// }

// int check() {
// 	//부등호 조건이 맞지 않다면 0을 리턴하고 맞다면 1을 리턴
// 	for (int i = 0; i < strlen(str); i++) {
// 		if (str[i] == '<') {
// 			if (copy[i] >= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 		else if (str[i] == '>') {
// 			if (copy[i] <= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 	}
// 	return 1;
// }

// //파이썬 풀이
// import sys
// import heapq
// import math
// from collections import deque
// sys.setrecursionlimit(1001*1001)

// n = int(input())
// arr = list(input().split())
// res = []
// ch  = [0]*(11) #숫자 사용여부 체크 배열

// #go(숫자사용 체크배열,부등호배열 인덱스,내부 부등호 왼쪾에 들어갈 숫자,답 기록 배열)
// def go(ch,idx,cNum,ans):
//     if idx == n: # 지금까지 3개 넣었다는 의미이다 
//         res.append(''.join(map(str,ans)))
//     else:
//         for i in range(0,10): #부등호 오른쪽에 들어갈 숫자 i, 현재 부등호에서 0,9까지 숫자 대입해보기 부등호 만족하면 다음 재귀함수 호출
//             if ch[i] == 0 :
//                 if arr[idx] == '<' and cNum < i:
//                     ch[i] = 1
//                     go(ch,idx+1,i,ans + [i]) ans = [1]
//                     ch[i] = 0
//                 if arr[idx] == '>' and cNum > i:
//                     ch[i] = 1
//                     go(ch,idx+1,i,ans + [i])
//                     ch[i] = 0

// for i in range(0,10):
//     ch[i] = 1
//     go(ch,0,i,[i])
//     ch[i] = 0

// print(res[-1])
// print(res[0])

// // //https://www.acmicpc.net/problem/2529

// #include<stdio.h>
// #include<string.h>

// void swap(int a, int b);
// void dfs(int flag, int start, int end);
// int check();
// void permutaion(int flag, int start, int end);

// char str[11], max[11], min[11], copy[11];
// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	int k, i;
// 	scanf("%d", &k);
// 	//부등호의 개수가 k면 숫자는 k+1
// 	for (i = 0; i <= k; i++) {
// 		if (i != k) {
// 			getchar();
// 			str[i] = getchar();
// 		}
// 		else str[i] = NULL;
// 		//부등호의 수 + 1만큼의 수를 
// 		//최대 값에서는 9부터 아래로 하나씩 입력
// 		//최소 값에서는 0부터 위로 하나씩 입력
// 		max[i] = '9' - k + i;
// 		min[i] = '0' + k - i;
// 	}

// 	max[i] = NULL;
// 	min[i] = NULL;
// 	strcpy(copy, max);
// 	dfs(1, 0, k);
// 	strcpy(copy, min);
// 	dfs(0, 0, k);
// 	printf("%s\n%s", max, min);
// 	return 0;
// }

// void swap(int a, int b) {
// 	char tmp;
// 	tmp = copy[a];
// 	copy[a] = copy[b];
// 	copy[b] = tmp;
// }

// //flag 1이면 최대값 구하기
// //flag 0이면 최소값 구하기
// void dfs(int flag, int start, int end) {
// 	//n이 숫자 배열의 범위를 벗어났을 경우 이제 모두 정렬한 상태
// 	//정렬된 상태에서 부등호와 맞는지 체크하고 맞다면 현재값이 최대값봐 비교하여 최대값 구하기
// 	if (start == end + 1) {
// 		//n ==1 i=0 기준으로 모든 정렬을 완료 후 현재 값에 이상있는지 체크
// 		//부등호 값에 이상이 없이 숫자 배열이 되었다면 최대 최소 비교
// 		if (check()) {
// 			//flag 1 최대값 체크, flat 0 최소값 체크
// 			if (flag) {
// 				//strcmp(string compare) 문자열 비교 함수 
// 				//strcmp(str1, str2);  
// 				//str1 < str2 인 경우에는 음수 반환
// 				if (strcmp(max, copy) < 0) {
// 					strcpy(max, copy);
// 				}
// 			}
// 			else {
// 				//str1 > str2 인 경우에는 양수 반환
// 				if (strcmp(min, copy) > 0) {
// 					strcpy(min, copy);
// 				}
// 			}
// 		}
// 	}
// 	//모든 경우의 수 배열하기
// 	//순열 짜기 기본 코드 변형
// 	permutaion(flag,start,end);
// }
// void permutaion(int flag, int start, int end){
// 	for (int i = start; i <= end; i++) {
// 		swap(start, i);
// 		dfs(flag, start + 1, end);
// 		swap(start, i); //다시 원래 위치로 되돌리기
// 	}
// }

// int check() {
// 	//부등호 조건이 맞지 않다면 0을 리턴하고 맞다면 1을 리턴
// 	for (int i = 0; i < strlen(str); i++) {
// 		if (str[i] == '<') {
// 			if (copy[i] >= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 		else if (str[i] == '>') {
// 			if (copy[i] <= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 	}
// 	return 1;
// }



// // //https://www.acmicpc.net/problem/2529

// #include<stdio.h>
// #include<string.h>

// void swap(int a, int b);
// void dfs(int flag, int start, int end);
// int check();

// char str[11], max[11], min[11], copy[11];
// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	int k, i;
// 	scanf("%d", &k);
// 	//부등호의 개수가 k면 숫자는 k+1
// 	for (i = 0; i <= k; i++) {
// 		if (i != k) {
// 			getchar();
// 			str[i] = getchar();
// 		}
// 		else str[i] = NULL;
// 		//부등호의 수 + 1만큼의 수를 
// 		//최대 값에서는 9부터 아래로 하나씩 입력
// 		//최소 값에서는 0부터 위로 하나씩 입력
// 		max[i] = '9' - k + i;
// 		min[i] = '0' + k - i;
// 	}

// 	max[i] = NULL;
// 	min[i] = NULL;
// 	strcpy(copy, max);
// 	dfs(1, 0, k);
// 	strcpy(copy, min);
// 	dfs(0, 0, k);
// 	printf("%s\n%s", max, min);
// 	return 0;
// }

// void swap(int a, int b) {
// 	char tmp;
// 	tmp = copy[a];
// 	copy[a] = copy[b];
// 	copy[b] = tmp;
// }

// //flag 1이면 최대값 구하기
// //flag 0이면 최소값 구하기
// void dfs(int flag, int start, int end) {
// 	//n이 숫자 배열의 범위를 벗어났을 경우 이제 모두 정렬한 상태
// 	//정렬된 상태에서 부등호와 맞는지 체크하고 맞다면 현재값이 최대값봐 비교하여 최대값 구하기
// 	if (start == end + 1) {
// 		//n ==1 i=0 기준으로 모든 정렬을 완료 후 현재 값에 이상있는지 체크
// 		//부등호 값에 이상이 없이 숫자 배열이 되었다면 최대 최소 비교
// 		if (check()) {
// 			//flag 1 최대값 체크, flat 0 최소값 체크
// 			if (flag) {
// 				//strcmp 문자열 비교 함수 
// 				//strcmp(str1, str2);  
// 				//str1 < str2 인 경우에는 음수 반환
// 				if (strcmp(max, copy) < 0) {
// 					strcpy(max, copy);
// 				}
// 			}
// 			else {
// 				//str1 > str2 인 경우에는 양수 반환
// 				if (strcmp(min, copy) > 0) {
// 					strcpy(min, copy);
// 				}
// 			}
// 		}
// 	}

// //copy = [a,b,c]
// //start = 0, end = k;
// //
// 	//모든 경우의 수 배열하기
// 	//순열 짜기 기본 코드
// 	for (int i = start; i <= end; i++) {
// 		swap(start, i);
// 		dfs(flag, start + 1, end);
// 		swap(start, i); //다시 원래 위치로 되돌리기
// 	}
// }

// int check() {
// 	//부등호 조건이 맞지 않다면 0을 리턴하고 맞다면 1을 리턴
// 	for (int i = 0; i < strlen(str); i++) {
// 		if (str[i] == '<') {
// 			if (copy[i] >= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 		else if (str[i] == '>') {
// 			if (copy[i] <= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 	}
// 	return 1;
// }

// #include<stdio.h>
// #include<string.h>

// void swap(int a, int b);
// void bf(int flag, int start, int end);
// int check();

// char str[11], max[11], min[11], copy[11];
// int main() {
// 	//freopen("input.txt", "rt", stdin);
// 	int k, i;
// 	scanf("%d", &k);
// 	for (i = 0; i <= k; i++) {
// 		if (i != k) {
// 			getchar();
// 			str[i] = getchar();
// 		}
// 		else str[i] = NULL;
// 		//부등호의 수 + 1만큼의 수를 
// 		//최대 값에서는 9부터 아래로 하나씩 입력
// 		//최소 값에서는 0부터 위로 하나씩 입력
// 		max[i] = '9' - k + i;
// 		min[i] = '0' + k - i;
// 	}
// 	max[i] = NULL;
// 	min[i] = NULL;
// 	strcpy(copy, max);
// 	bf(1, 0, k);
// 	strcpy(copy, min);
// 	bf(0, 0, k);
// 	printf("%s\n%s", max, min);
// 	return 0;
// }

// void swap(int a, int b) {
// 	char tmp;
// 	tmp = copy[a];
// 	copy[a] = copy[b];
// 	copy[b] = tmp;
// }

// //flag 1이면 최대값 구하기
// //flag 0이면 최소값 구하기
// void bf(int flag, int start, int end) {
// 	//n이 숫자 배열의 범위를 벗어났을 경우 이제 모두 정렬한 상태
// 	//정렬된 상태에서 부등호와 맞는지 체크하고 맞다면 현재값이 최대값봐 비교하여 최대값 구하기
// 	if (start == end + 1) {
// 		//n ==1 i=0 기준으로 모든 정렬을 완료 후 현재 값에 이상있는지 체크
// 		//부등호 값에 이상이 없이 숫자 배열이 되었다면 최대 최소 비교
// 		if (check()) {
// 			//flag 1 최대값 체크, flat 0 최소값 체크
// 			if (flag) {
// 				//strcmp 문자열 비교 함수 
// 				//strcmp(str1, str2);  
// 				//str1 < str2 인 경우에는 음수 반환
// 				if (strcmp(max, copy) < 0) {
// 					strcpy(max, copy);
// 				}
// 			}
// 			else {
// 				//str1 > str2 인 경우에는 양수 반환
// 				if (strcmp(min, copy) > 0) {
// 					strcpy(min, copy);
// 				}
// 			}
// 		}
// 	}
// 	//모든 경우의 수 배열하기
// 	//순열 짜기 기본 코드
// 	for (int i = start; i <= end; i++) {
// 		swap(i, start);
// 		bf(flag, start + 1, end);
// 		swap(i, start); //다시 원래 위치로 되돌리기
// 	}
// }
// int check() {
// 	for (int i = 0; i < strlen(str); i++) {
// 		if (str[i] == '<') {
// 			if (copy[i] >= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 		else if (str[i] == '>') {
// 			if (copy[i] <= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 	}
// 	return 1;
// }



// #include<stdio.h>
// #include<string.h>

// void swap(int a, int b);
// void bf(int flag, int n);
// int check();

// char str[11], max[11], min[11], copy[11];

// int main() {
// 	int k, i;
// 	scanf("%d", &k);
// 	for (i = 0; i <= k; i++) {
// 		if (i != k) {
// 			getchar();
// 			str[i] = getchar();
// 		}
// 		else str[i] = NULL;
//         //부등호의 수 + 1만큼의 수를 
//         //최대 값에서는 9부터 아래로 하나씩 입력
//         //최소 값에서는 0부터 위로 하나씩 입력
// 		max[i] = '9' - k + i;
// 		min[i] = '0' + k - i;
// 	}
// 	max[i] = NULL;
// 	min[i] = NULL;
// 	strcpy(copy, max);
// 	bf(1, k + 1);
// 	strcpy(copy, min);
// 	bf(0, k + 1);
// 	printf("%s\n%s", max, min);
//     	return 0;
// }

// void swap(int a, int b) {
// 	char tmp;
// 	tmp = copy[a];
// 	copy[a] = copy[b];
// 	copy[b] = tmp;
// }
// //flag 1이면 최대값 구하기
// //flag 0이면 최소값 구하기
// void bf(int flag, int n) {
// 	if (n == 1) {
//         //n ==1 i=0 기준으로 모든 정렬을 완료 후 현재 값에 이상있는지 체크
//         //부등호 값에 이상이 없이 숫자 배열이 되었다면 최대 최소 비교
        
// 		if (check()) {
// 			if (flag) {
//                 //strcmp 문자열 비교 함수 
//                 //strcmp(str1, str2);  
//                 //str1 < str2 인 경우에는 음수 반환
// 				if (strcmp(max, copy) < 0) {
// 					strcpy(max, copy);
// 				}
// 			}
// 			else {
//                 //str1 > str2 인 경우에는 양수 반환
// 				if (strcmp(min, copy) > 0) {
// 					strcpy(min, copy);
// 				}
// 			}
// 		}
// 	}
//     //모든 경우의 수 배열하기
//     //순열 짜기 기본 코드
// 	for (int i = 0; i < n; i++) {
// 		swap(i, n - 1);
// 		bf(flag, n - 1);
// 		swap(i, n - 1); //다시 원래 위치로 되돌리기
// 	}
// }
// int check() {
// 	for (int i = 0; i < strlen(str); i++) {
// 		if (str[i] == '<') {
// 			if (copy[i] >= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 		else if(str[i] == '>'){
// 			if (copy[i] <= copy[i + 1]) {
// 				return 0;
// 			}
// 		}
// 	}
// 	return 1;
// }


//https://ggodong.tistory.com/138 순열 구현하기
// #include <stdio.h>

// int arr[4] = { 1, 2, 3, 4 };
// int len = 4;

// void swap(int a, int b) {
// 	int temp = arr[a];
// 	arr[a] = arr[b];
// 	arr[b] = temp;
// }

// void permu(int N) {
// 	if (N == 3) {
// 		for (int i = 0; i < 4; i++) {
// 			printf("%d", arr[i]);
// 		}
// 		printf("\n");
// 	}
// 	else {
// 		for (int i = N; i < 4; i++) {
// 			swap(i, N);
// 			permu(N + 1);
// 			swap(i, N);
// 		}
// 	}
// }

// int main(void) {
// 	permu(0);
// }