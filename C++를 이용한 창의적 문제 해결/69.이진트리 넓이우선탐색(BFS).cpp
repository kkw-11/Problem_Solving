#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
//front와 rear를 활용해 배열 Q를 자료구조 queue를 간단하게 구현
int Q[100], front = -1, rear = -1, ch[10];
vector<int> map[10];//map이라는 벡터가 10개 생성
void bfs(int start) {
    int x;
    Q[++rear] = start;
    ch[0] = start;
    while (front < rear) {
        x = Q[++front];
        printf("%d", x);
        for (int i = 0; i < map[x].size(); ++i) {
            if (ch[map[x][i]] == 0) {
                ch[map[x][i]] = 1;
                Q[++rear] = map[x][i];
            }
        }
    }
}
int main() {
    freopen("input.txt", "rt", stdin);
    int a, b;
    for (int i = 0; i < 6; ++i) {
        // 간선정보 입력 받고
        scanf("%d %d", &a, &b);
        //무방향 그래프 연결리스트 방식으로 생성
        map[a].push_back(b);
        map[b].push_back(a);
    }


    bfs(1);
    return 0;
}

// #include<stdio.h>
// #include<vector>
// #include<algorithm>
// using namespace std;
// int Q[100], front = -1, rear = -1, ch[10];
// vector<int> map[10];//map이라는 벡터가 10개 생성
// void bfs(int start){
//   Q[++rear] = start;
//     ch[0] = start;
//     while(front<rear){
//         int x = Q[++front];
//         printf("%d",x);
//         for(int i = 0;i<map[x].size();++i){
//             if(ch[map[x][i]]==0){
//                 ch[map[x][i]] = 1;
//                 Q[++rear] = map[x][i];
//             }
//         }
//     }


// }
// int main(){
//     int a,b,x;
//     for(int i = 0;i<6;++i){
//         scanf("%d %d",&a,&b);
//         map[a].push_back(b);
//         map[b].push_back(a);
//     }


//     bfs(1);
//       return 0;
// }