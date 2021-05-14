//https://www.acmicpc.net/problem/16234

#include <stdio.h>

int drow[] = {-1,1,0,0};
int dcol[] = {0,0,-1,1};
int map[51][51], allycheck[51][51];
int cnt, sum, allycount, N,L,R;

int main(){
    freopen("input.txt","rt",stdin);
    //입력값 받기
    scanf("%d%d%d",&N,&L,&R);

    for(int i = 0; i<N;++i){
        for(int j = 0 ; j<N;++j){
            scanf("%d",&map[i][j]);
        }
    }
    //연합국 인지 확인(연합국 allycheck 배열 0->1, 연합국 아니면(상하좌우 차가 모두 문제의 주어진 범위에 속하지 않으면) -1)

    //연합국의 각 인구 계산

    //연합국 인구 갱신

    //위 과정 반복
    return 0;
}