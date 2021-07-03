//https://www.acmicpc.net/problem/1339
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int N,arr[30]={0,};
	cin >> N;
	
	for(int i=0;i<N;i++){
		string s;
		cin >> s;

        //11111
		//ABCD
		//GCDE
		//arr[0]//A = 1000
		//arr[1]//B = 100
		//arr[2]//C = 100 + 1000 = 1100
		//
        //다음 문자 입력 받은 다음 부터는 다시 자리수 부여를 위해 k=1 초기화
		int k = 1;
        //arr배열에 A부터 0번 인덱스에 문자 자리 부여
        //ex)0번 인덱스는 A, 1번 인덱스는 B, 2번 인덱스는 C...
        //각 문자마다 자리수 부여
        //-로 자리수 부여하는 이유는 sort함수 오름차순 정렬 때문

		for(int j=s.length() - 1;j>=0;j--){
			arr[s[j] - 'A'] -= k;
			k *= 10;
		}
	}	

	//A-1000 , B-100 C-1100, D-11. E-1, F 0, G-1000
	//0,         000         0 1 11 100 1000 1100[]
	sort(arr, arr+30);
	
	int result=0;

	//-1100*9 -1000*8, -1000*7, -11*6 -1*6 0 0 0 0 0 
	for(int i=0;i<10;i++){
		result += -arr[i]*(9-i);
	}
	
	cout << result;
	return 0;
}
