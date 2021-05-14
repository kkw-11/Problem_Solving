#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int Q[100], front = -1, rear = -1, ch[10];
vector<int> map[10];//map이라는 벡터가 10개 생성

int main(){
    int a,b,x;
    for(int i = 0;i<6;++i){
        scanf("%d %d",&a,&b);
        map[a].push_back(b);
        map[b].push_back(a);
    }

    Q[++rear] = 1;
    ch[0] = 1;
    while(front<rear){
        x = Q[++front];
        printf("%d",x);
        for(int i = 0;i<map[x].size();++i){
            if(ch[map[x][i]]==0){
                ch[map[x][i]] = 1;
                Q[++rear] = map[x][i];
            }
        }
    }

    return 0;
}