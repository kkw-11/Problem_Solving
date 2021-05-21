//https://www.acmicpc.net/problem/2688

#include <stdio.h>

bool check(int n, int digit){

    int rightNum, leftNum;
    bool incresingNum = true;
    while (n)
    {
        rightNum = n % 10; //3
        n /= 10;    //12
        leftNum = n % 10; //2
        if (leftNum > rightNum){
            incresingNum = false;
            break;
        }

    }

    return incresingNum;
}

int main(){

    if (check(321, 3))
        printf("Yes incresing number");
    else
        printf("No incresing number ")

    return 0;
}