//https://programmers.co.kr/learn/courses/18/lessons/1878?language=c

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// v_row_len은 2차원 배열 v의 행(세로) 길이입니다.
// v_col_len은 2차원 배열 v의 열(가로) 길이입니다.
// v[i][j]는 v의 i번째 행의 j번째 열에 저장된 값을 의미합니다.
int* solution(int **v, size_t v_row_len, size_t v_col_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    
    int* answer = (int*)calloc(2,sizeof(4));
    for(int i =0;i<3;++i){
        answer[0] ^= v[i][0]; 
        answer[1] ^= v[i][1]; 
    }
    return answer;
}
