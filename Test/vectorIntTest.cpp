#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<vector <int>> vd;
    vector<int> v1;
    vector<int> v2;

    v1.push_back(11);
    v1.push_back(22);

    for(int i = 0;i<5;++i){
        v2.push_back(i);
    }

    vd.push_back(v1);
    vd.push_back(v2);

    printf("v1size:%d\n",v1.size());
    printf("v2size:%d\n",v2.size());

    for(int i = 0;i<vd.size();++i){
        for(int j = 0; j<vd[i].size();++j){
            printf("%d ",vd[i][j]);
        }
        printf("\n");
    }


    return 0;
}