//https://www.acmicpc.net/problem/16234

#include <stdio.h>

int drow[] = {-1,1,0,0};
int dcol[] = {0,0,-1,1};
int map[51][51], allycheck[51][51];
int cnt, sum, allycount, N,L,R, r,c, sub,flag;

void allycheckfunc(){
    //i,j는 map의 현재 위치를 나타내는 변수
    //k는 현재위치로부터 상하좌우 이동을 어디로 할지 정하는 변수
    for(int i = 0;i<N;++i){
        for(int j = 0; j<N;++j){
            //i,j는 현재위치,r,c는 이웃 위치
            for(int k = 0;k<4;++k){
                r = i + drow[k];
                c = j + dcol[k];
                if(r>=0&&r<N && c>=0&&c<N){
                     if((map[r][c] - map[i][j])>=L && (map[r][c] - map[i][j])<=R){
                        if(allycheck[r][c] != 1){
                            allycheck[r][c] = 1;
                            sum += map[r][c];
                            ++allycount;
                        }
                        if(allycheck[i][j] != 1){
                            allycheck[i][j] = 1;
                            sum += map[i][j];
                            ++allycount;
                        }

                     }
                }
            }
        }
    }
}
int renewal(){
    for(int i = 0;i<N;++i){
        for(int j = 0;j<N;++j){
            if(allycheck[i][j] == 1){
                map[i][j] = sum/allycount;
                flag = 1;
            }
        }
    }
    return flag; 
}
void reset(){
    flag = 0;
    for(int i = 0; i<N;++i){
        for(int j = 0 ; j<N;++j){
            allycheck[i][j] = 0;
        }
    }
}
int main(){
    //freopen("input.txt","rt",stdin);
    //입력값 받기
    scanf("%d%d%d",&N,&L,&R);

    for(int i = 0; i<N;++i){
        for(int j = 0 ; j<N;++j){
            scanf("%d",&map[i][j]);
        }
    }
    while(1){
        //연합국 인지 확인(연합국 allycheck 배열 0->1, 연합국 아니면(상하좌우 차가 모두 문제의 주어진 범위에 속하지 않으면) -1)
        //연합국의 각 인구 계산
        allycheckfunc();

        //연합국 인구 갱신
        flag = renewal();

        if(flag)
           ++cnt;
        else 
           break;

        //리셋 후 위 과정 반복
        reset();
    }
    
    printf("%d",cnt);
    
    return 0;
}