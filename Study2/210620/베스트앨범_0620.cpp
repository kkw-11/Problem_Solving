//https://programmers.co.kr/learn/courses/30/lessons/42579?language=cpp

#include <string>
#include <vector>
#include <map>
using namespace std;
 
vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
   
    //각 장르별로 총 재생횟수 저장 해쉬
    map<string, int> genreTotalPlays;
    //각 장르별로 무슨 노래가 몇 번씩 재생됐는지
    map<string, map<int, int>> musicLists;  //musiclic<장르:<노래번호,플레이횟수>>

    //들어온 리스트만큼 반복
    for (int i = 0; i < genres.size(); i++) {
        //music map에 장르별로 횟수추가
        //i번 노래의 장르, 플레이스 누적 <"classic":1450> <"pop":3100>
        genreTotalPlays[genres[i]] += plays[i]; 

        //musiclist map에 노래번호와 플레이횟수 추가
        // musiclist <장르:<노래번호,플레이횟수>> 
        //<"classic", 0, 500> <"classic",2, 150>  <"classic",3, 800>
        //<"pop", 1, 600> <"pop", 4, 2500>
        musicLists[genres[i]][i] = plays[i]; //musiclic<장르:<노래번호,플레이횟수>>
    }
    
    //장르가 다 없어질 때까지 반복
    while (genreTotalPlays.size() > 0) {
        string genre;
        int max = 0;

        //장르중에서 제일 높은 것 찾기
        for (auto genreTotalPlay : genreTotalPlays){
            if (max < genreTotalPlay.second){
                max = genreTotalPlay.second;
                genre = genreTotalPlay.first;
            }
        }

        //2곡을 넣어야 하므로 2번 반복
        for (int i = 0; i < 2; i++){
            int val = 0, idx = -1;

              //<"classic", 0, 500> <"classic",2, 150>  <"classic",3, 800>
           //<"pop", 1, 600> <"pop", 4, 2500>
            //해당 장르 노래중에 노래중에서 제일 높은것 찾기
            for (auto musicList : musicLists[genre]) {
                if (val < musicList.second) {
                    val = musicList.second;
                    idx = musicList.first;
                }
            }

            //만약 노래가 0~1곡밖에 없다면 반복문 탈출
            if (idx == -1)    
                break;

            //리턴할 리스트에 노래번호 추가
            answer.push_back(idx);
            musicLists[genre].erase(idx);

        }
        //map 에서 사용한 장르삭제
        genreTotalPlays.erase(genre);
    }
    
    return answer;
}