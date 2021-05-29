//https://programmers.co.kr/learn/courses/30/lessons/42584?language=cpp
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
  
    vector<int> answer;
    
    for(int i = 0; i<prices.size()-1;++i){
        int time = 0;
        for(int j = i+1; j<prices.size();++j){
            if(prices[i]<=prices[j])
                ++time;
            else{
                ++time;
                break;   
            }
             
        }
        answer.push_back(time);
    }
    
    answer.push_back(0);
 
    return answer;
}