////55.기차운행(stack)
//#include <stdio.h>
//#define MAX 30
//
//int stack[MAX] = { 0 };
//int top;
//
//void InitStack() {
//	top = 0;
//}
//
//void Push(int data) {
//	if (top == MAX) return;
//	stack[top++] = data;
//}
//
//int Pop() {
//	if (top == 0) return -1;
//	return stack[--top];
//}
//int Empty() {
//	if (top == 0) return 1;
//	return 0;
//}
//
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int N;
//	scanf("%d", &N);
//
//	int i, m, check = 1, j = 0;
//	char ch[61];
//
//	for (i = 0; i < N; ++i) {
//		scanf("%d", &m);
//		Push(m);
//		ch[j++] = 'P';
//		while (1) {
//			if (Empty()) break;
//			if (stack[top - 1] == check) {
//				Pop();
//				ch[j++] = 'O';
//				++check;
//			}
//			else
//				break;
//		}
//	}
//	if (!Empty())
//		printf("impossible\n");
//	else {
//		ch[j] = '\0';
//		printf("%s", ch);
//	}
//
//
//	return 0;
//
//}

////55.기차운행(stack)
//#include <stdio.h>
//#include <stack>
//#define MAX 30
//
//int stack[MAX] = { 0 };
//int top;
//
//void InitStack() {
//	top = 0;
//}
//
//void Push(int data) {
//	if (top == MAX) return;
//	stack[top++] = data;
//}
//
//int Pop() {
//	if (top == 0) return -1;
//	return stack[--top];
//}
//int Empty() {
//	if (top == 0) return 1;
//	return 0;
//}
//
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int N;
//	scanf("%d", &N);
//	int a[30];
//	char ch[61];
//	int impossible = 0, check = 1;
//
//	for (int i = 0; i < N; ++i) {
//		scanf("%d", &a[i]);
//	}
//	InitStack();
//
//	int i = 0, j = 0;
//	//for (int i = 0; i < N; ++i) {
//	while (1) {
//		if (i < N) {
//			Push(a[i++]);
//			ch[j++] = 'P';
//		}
//		if (i == N && stack[top - 1] > check) {//더이상 stack에 push 할 값이 없고 stack에 값은 입력되어야 할 값보다 클 경우 불가능
//			impossible = 1;
//			break;
//		}
//
//		while (1) {
//			if (Empty()) break;
//			if (check == stack[top - 1]) {
//				Pop();
//				ch[j++] = 'O';
//				++check;
//			}
//			else
//				break;
//		}
//
//		if (j == 2 * N)
//			break;
//	}
//
//	if (impossible)
//		printf("impossible");
//	else {
//		ch[j] = '\0';
//		printf("%s", ch);
//
//	}
//
//	return 0;
//
//}

////55.기차운행(stack)
//#include <stdio.h>
//#include <stack>
//#define MAX 30
//
//int stack[MAX] = { 0 };
//int top;
//
//void InitStack() {
//	top = 0;
//}
//
//void Push(int data) {
//	if (top == MAX) return;
//	stack[top++] = data;
//}
//
//int Pop() {
//	if (top == 0) return -1;
//	return stack[--top];
//}
//
//int main() {
//	//freopen("input.txt", "rt", stdin);
//	int N;
//	scanf("%d", &N);
//	int a[30];
//	char ch[61];
//	int impossible = 0, check = 1;
//
//	for (int i = 0; i < N; ++i) {
//		scanf("%d", &a[i]);
//	}
//	InitStack();
//
//	int i = 0, j = 0;
//	while (1) {
//		if (i < N) {
//			Push(a[i++]);
//			ch[j++] = 'P';
//		}
//		if (i == N && stack[top - 1] > check) {
//			impossible = 1;
//			break;
//		}
//
//		while (1) {
//			if (stack[top - 1] == check) {
//				Pop();
//				ch[j++] = 'O';
//				++check;
//			}
//			else
//				break;
//		}
//
//		if (j == 2 * N)
//			break;
//	}
//
//	if (impossible)
//		printf("impossible");
//	else {
//		ch[j] = '\0';
//		printf("%s", ch);
//
//	}
//
//	return 0;
//
//}
