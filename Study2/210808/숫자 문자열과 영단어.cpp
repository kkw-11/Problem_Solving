// https://programmers.co.kr/learn/courses/30/lessons/81301

#include <string> 
#include <vector> 
#include <map> 
using namespace std;

int solution(string s) {
	int answer = 0;
	map<string, int> hash;

	hash["zero"] = 0;
	hash["one"] = 1;
	hash["two"] = 2;
	hash["three"] = 3;
	hash["four"] = 4;
	hash["five"] = 5;
	hash["six"] = 6;
	hash["seven"] = 7;
	hash["eight"] = 8;
	hash["nine"] = 9;

	string temp = "";

	for (int i = 0; i < s.size(); i++) {
		if (s[i] >= '0' && s[i] <= '9') //아스키 '0' : 48
			answer = answer * 10 + s[i] - '0';
		else {
			temp += s[i]; //tsdfsad
			if (hash.find(temp) != hash.end()) { //mp.find로 찾지 못하면 mp.end() 반환, 찾으면 해당 value 반환
				answer = answer * 10 + hash[temp]; //123
				temp.clear();
			}
		}
	}

	return answer;
}
