//https://programmers.co.kr/learn/courses/30/lessons/42578

#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes){
    int answer = 1;
    map<string, int> m;
    for(vector<string> c : clothes){
        ++m[c[1]];
    }
    map<string, int>::iterator it;

    //상의 3, 하의 2, 모자 4 1* (3+1)* (2+1)* (4*1)
    for(it = m.begin();it !=m.end();++it){
        answer *= (it->second +1);
    }

    return answer - 1;
}