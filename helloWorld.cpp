#include <string> 
#include <vector> 
using namespace std;
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 }; 
bool chk;

void find(vector<string>& v, int x, int y, int X, int Y, int cnt)
{
	if (cnt == 2)
		return;
	for (int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && v[nx][ny] != 'X')
		{
			if (nx == X && ny == Y) continue;
			if (v[nx][ny] == 'P') {
				chk = false; 
                return;
			}
			find(v, nx, ny, X, Y, cnt + 1);
		}
	}
}

vector<int> solution(vector<vector<string>> places) {
	vector<int> answer;
	for (auto v : places) {
		bool flag = true;
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				if (v[i][j] == 'P') {
					chk = true; find(v, i, j, i, j, 0);
					if (!chk) flag = false;
				}
			}
		} if (flag) answer.push_back(1);
		else answer.push_back(0);
	}
	return answer;
}