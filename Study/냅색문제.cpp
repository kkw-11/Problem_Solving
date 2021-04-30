//https://www.acmicpc.net/problem/1450
#include<cstdio>
#include<algorithm>
using namespace std;

#define mxl 30
#define mxn 30
int sum1[mxl], sum2[mxl], l1, l2, a[mxn];

void dfs(int start, int end, int sum, int flag, int m) {
    if (sum > m) return;
    if (start == end) {
        if (flag == 1) sum1[l1++] = sum;
        else sum2[l2++] = sum;
        return;
    }
    dfs(start + 1, end, sum, flag, m);
    dfs(start + 1, end, sum + a[start], flag, m);
}
int main() {
    freopen("input.txt", "rt", stdin);
    int n, m, cnt = 0;
    scanf("%d%d", &n, &m);

    //부분집합 2^n n개의 물건에
    //2^30 -> 2^15, 2^15 ->2^16 
    for (int i = 0; i < n / 2; i++) scanf("%d", &a[i]);
    dfs(0, n / 2, 0, 1, m);
    sort(sum1, sum1 + l1);

    for (int i = n / 2; i < n; i++) scanf("%d", &a[i - (n / 2)]);
    dfs(0, n - (n / 2), 0, 2, m);
    sort(sum2, sum2 + l2);
////////
//sum1[0]

//
    for (int i = 0, j = l2 - 1; i < l1 && j >= 0; i++) {
        while (sum1[i] + sum2[j] > m) j--;
        cnt += j + 1; //j sum1[i] + sum2[j] <= m // sum1[i] + sum2[j]>m 

        //
    }
    printf("%d", cnt);
    return 0;
}


// // https://www.acmicpc.net/problem/1450

// //pseudo code
// //냅색 알고리즘 인프런 강좌 학습하고 보기
// #include <stdio.h>
// int sum, i, j, c, n, cnt;
// int num[30];

// //10 3
// //2 1 1 3 1 1 1 4 5 
// //i값이 N이 되었을 때 
// //3 -> --2

// void go(int c, int i, int j, int sum) {
//     if (i == n) return;

//     if (c == sum) {
//         ++cnt;
//         ++j;
//         sum = 0;
//         if (j == n) {
//             ++i;
//             if (i == n) return;
//             j = i + 1;
//            sum = sum + num[i];
//         }
//     }
//     else if (c < sum) {
//         sum -= num[j];
//         ++j;
//         if (j == n) {
//             sum = 0;
//             ++i;
//             if (i == n) return;
//             j = i + 1;
//             sum = sum + num[i];
//         }
//     }

//     go(--c, i, j, sum + num[j]);

// }


// int main() {
//     freopen("input.txt", "rt", stdin);
//     scanf("%d%d", &n, &c);
//     for (int k = 0; k < n; ++k) {
//         scanf("%d", &num[k]);
//     }

//     j = i + 1;
//     sum += num[i];
//     go(c, i, j, sum);

//     printf("%d", cnt);

//     return 0;
// }



// # 간편 설명
// '''
// 이는 array의 possible한 subsum 들의 개수를 구하는 문제와 같다 

// 특정 arr의 subsum을 구한다는 것은, 
// 다른 말로 하면, 부분집합을 구한 이후, 그 해당 부분집합 각각의 원소들의 합을 구하는 것과 같다

// 다른 말로 하면, 사실, 부분집합을 구하는 것이다

// 1) Brute Force
// - 부분집합을 구한다는 것은, 각각의 원소가 부분집합에 속할지 안속할지를 결정한다는 것
// 즉, n개의 원소가 있다면 각각의 원소에 대해서 
// 1. 속할지 2. 안속할지 --> 를 결정하는 것과 같다는 것이다 

// 따라서 2 ^ n 만큼의 시간이 소요된다

// 2) Meet in the middle
// maximum subsum array를 구할 때 사용하는 개념이다 

// 해당 n개의 원소를 반으로 쪼갠다
// A : [0 ~ n//2]
// B : [n//2 + 1 ~ n]

// 각각의 subsum들을 구하여,
// 각각의 subsumA, subsumB 라는 array 에 넣는다

// subsumB를 sort 한다

// subsumA 내 각각의 원소에 대해서 ,
// sort된 subsumB를 이진 탐색 하여 , 
// 최대의 maximum을 구하는 과정을 진행하면 된다 

// '''

// import sys
// import heapq
// import math
// from collections import deque
// sys.stdin = open("input.txt", "rt")
// sys.setrecursionlimit(1001*1001)

// n, c = map(int, input().split())
// a = list(map(int, input().split()))
// res = 0

// midLen = len(a) // 2

// subA = a[:midLen]
// sSumA = []
// subB = a[midLen:]
// sSumB = []


// def subSum(L, idx, sum, arr, sSumA):
//     if L == idx:
//         sSumA.append(sum)
//         return
//     else:
//         # 선택
//         subSum(L, idx+1, sum + arr[idx], arr, sSumA)
//         # 선택 x
//         subSum(L, idx+1, sum, arr, sSumA)


// def upperBound(st, ed, target, a):
//     # 1) ed
//     # 2) a[mid] < target , a[mid] == target  --> 같은 알고리즘
//     '''
//     [2,4,4,7,9]
//     a[4]
//     a[5]

//     target = 10

//     '''
//     while st < ed:
//         mid = (st+ed) // 2
//         if a[mid] <= target:
//             # target보다 큰 값을 지닌 원소를 찾아 계속 뒤로
//             st = mid + 1
//         elif a[mid] > target:
//             ed = mid
//     return ed


// subSum(len(subA), 0, 0, subA, sSumA)
// subSum(len(subB), 0, 0, subB, sSumB)
// sSumB.sort()

// for elem in sSumA:
//     # c = 10 , elem = 4 , 6 target
//     target = c - elem
//     if c - elem < 0:
//         continue
//     # 여기서 끝의 위치를 의미하는 2번째 인자로, 일반적인 binary와 달리
//     # len(sSumB) - 1 을 넣어주면 안된다
//     # ex) [0,1] => '1'까지 가능하다면, 2라는 숫자가 return되어야 하는데
//     # 애초부터 len(sSumB) - 1 을 넣어주게 되면, 최대 1이라는 숫자밖에 return 되지 않는다

//     # c : 10
//     # sSumA => 1
//     # sSumB = [3,5,8] --> binary(0,2)

//     add = upperBound(0, len(sSumB), target, sSumB)
//     res += add
// print(res)