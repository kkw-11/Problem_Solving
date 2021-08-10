#include <cstdio>
#include <cstdlib>
#include <queue>
#include <algorithm>
using namespace std;

void PrintList(int list[]) {
	int size = list[0];
	printf("size:%d   [", size);
	for (int i = 1; i <= size; ++i) {
		printf("%5d ", list[i]);
	}
	printf("]\n");
}
void Swap(int& a, int& b) {
	int t = a;
	a = b;
	b = t;
}

void Push_heap(int list[]) {
	int size = ++list[0];
	int child = size;
	int parent = child / 2;
	while (child > 1) {
		if (list[parent] < list[child])
			Swap(list[parent], list[child]);
		else
			break;
		child = parent;
		parent = child / 2;

	}

}
void Make_heap(int list[], int size) {
	for (int i = 0; i < size; ++i) {
		Push_heap(list);
	}
}
void Pop_heap(int list[]) {
	int size = --list[0];
	Swap(list[1], list[size + 1]);
	int parent = 1;
	int child = parent * 2;

	while (child <= size) {
		if (child < size && list[child] < list[child + 1])
			child = child + 1;

		if (list[parent] < list[child])
			Swap(list[parent], list[child]);
		else
			break;
		parent = child;
		child = parent * 2;

	}

}
void Sort_heap(int list[],int size) {
	for (int i = 0; i < size; ++i) {
		Pop_heap(list);
	}

	for (int i = 1; i < size; ++i)
		printf("%5d", list[i]);
	printf("\n");
}
int main() {
	int list[10] = { 0, 50,60,30,10,20,90,70,58 };
	//int list[10] = { 5, 60,50,30,10,20,90,70,58 };

	PrintList(list);
	Make_heap(list, 8);

	Sort_heap(list, 8);
	PrintList(list);

	for (int i = 1; i <= 8; ++i) {
		printf("%5d ", list[i]);
	}
	printf("\n");

	system("pause");
	return 0;
}
