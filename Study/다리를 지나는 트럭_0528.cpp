//https://programmers.co.kr/learn/courses/30/lessons/42583

#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int remainingWeight = weight;
    int answer = 0;
    int crossingTruckWeight =0;
    int curTruckIdx = 0;
    queue<int> q;
        
    while(curTruckIdx != truck_weights.size()){
        
        ++answer;
        
        
        if(truck_weights[curTruckIdx]+ crossingTruckWeight <= weight){
            q.push(truck_weights[curTruckIdx]);
            crossingTruckWeight += truck_weights[curTruckIdx];
            ++curTruckIdx;
            
        }
        else{
            q.push(0);
        }
        
        if(q.size()==bridge_length){
            crossingTruckWeight-=q.front();

            q.pop();
        }
        
    }
    
    answer += bridge_length;
    
    return answer;
}