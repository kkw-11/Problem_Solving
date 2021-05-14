#include <stdio.h>

char copy[] = {'A','B','C'};

void permutaion(char arr[], int start, int end);
void printArray(char arr[], int size);
void swap(char arr[], int a, int b);


int main(){
    int size = sizeof(copy)/sizeof(char);

    printf("fist value:\n");
    printArray(copy,size);
    
    printf("start:\n");

    permutaion(copy,0,size-1);

    return 0;
}

void permutaion(char arr[], int start, int end){
    if(start == end+1){
       printArray(arr,end+1);
    }

    for(int i = start; i<=end;++i){
        swap(arr,start,i);
        permutaion(arr,start+1,end);
        swap(arr,start,i);
    }
}

void printArray(char arr[], int size){
        for(int i = 0;i<size;++i){
            printf("%c ",copy[i]);
        }
        printf("\n\n");
}

void swap(char arr[], int a, int b){
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
