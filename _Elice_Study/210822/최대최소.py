#include <cstdio>
#include <algorithm>
#define LM 100000
#define INF 2e9
using namespace std;
 
int N, M, a, b;
int maxTree[4 * LM], minTree[4 * LM];
 
int maxUpdate(int pos, int val, int node, int start, int end) {
    if (pos < start || end < pos)
        return maxTree[node];
    if (start == end)
        return maxTree[node] = val;
 
    int mid = (start + end) >> 1;
    int L = maxUpdate(pos, val, node * 2, start, mid);
    int R = maxUpdate(pos, val, node * 2 + 1, mid + 1, end);
    return maxTree[node] = max(L, R);
}
 
int maxQuery(int node, int start, int end, int qLeft, int qRight) {
    if (qRight < start || end < qLeft)
        return -INF;
    if (qLeft <= start && end <= qRight)
        return maxTree[node];
 
    int mid = (start + end) >> 1;
    int L = maxQuery(node * 2, start, mid, qLeft, qRight);
    int R = maxQuery(node * 2 + 1, mid + 1, end, qLeft, qRight);
    return max(L, R);
}
int minUpdate(int pos, int val, int node, int start, int end) {
    if (pos < start || end < pos)
        return minTree[node];
    if (start == end)
        return minTree[node] = val;
 
    int mid = (start + end) >> 1;
    int L = minUpdate(pos, val, node * 2, start, mid);
    int R = minUpdate(pos, val, node * 2 + 1, mid + 1, end);
    return minTree[node] = min(L, R);
}
int minQuery(int node, int start, int end, int qLeft, int qRight) {
    if (qRight < start || end < qLeft)
        return INF;
    if (qLeft <= start && end <= qRight)
        return minTree[node];
 
    int mid = (start + end) >> 1;
    int L = minQuery(node * 2, start, mid, qLeft, qRight);
    int R = minQuery(node * 2 + 1, mid + 1, end, qLeft, qRight);
    return min(L, R);
}
int main() {
    scanf("%d%d", &N, &M);
    
    for (int i = 1; i <= N; i++) {
        scanf("%d", &a);
        maxUpdate(i, a, 1, 1, N);
        minUpdate(i, a, 1, 1, N);
    }
 
    for (int i = 0; i < M; i++) {
        scanf("%d%d", &a, &b);
        printf("%d %d\n", minQuery(1, 1, N, a, b), maxQuery(1, 1, N, a, b));
    }
}