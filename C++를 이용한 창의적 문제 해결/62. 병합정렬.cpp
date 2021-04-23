#include<stdio.h>
int data[10];
int temp[10];
void mergeSort(int left,int right) {
    int mid;
    if (left < right) {
        mid = (left + right)/2;
        mergeSort(left, mid);
        mergeSort(mid+1, right);
        //자식노드(함수)들의 리턴이 완료되어야 수행되는 곳=>후위순회

        //자식노드에서 정렬된 두 배열을 병합하면서 정렬
        int p1= left, p2 = mid + 1,p3=left;
        while (p1 <= mid && p2<= right) {
            if (data[p1] < data[p2])
                temp[p3++] = data[p1++];
            else 
                temp[p3++] = data[p2++];
        }
        //남는 원소 담는 코드
        while(p1<=mid)
            temp[p3++] = data[p1++];
        while(p2<=right)
            temp[p3++] = data[p2++];

        for (int i = left; i <= right; ++i) {
            data[i] = temp[i];
        }

    }
    else {

    }

}
int main() {
    freopen("input.txt", "rt", stdin);
    int n;

    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &data[i]);
    }
    mergeSort(0, n - 1);
    for (int i = 0; i < n; ++i) {
        printf("%d ", data[i]);
    }

    return 0;
}