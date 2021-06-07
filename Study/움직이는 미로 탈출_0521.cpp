//https://www.acmicpc.net/problem/16954
#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

char map[8][8];
char tmp[8][8];

int dx[9] = {-1,-1,-1,0,1,1,1,0,0}; // 왼위 위 오위 오 오아 아 왼아 왼 가운데
int dy[9] = {-1,0,1,1,1,0,-1,-1,0};
int high = 0;

void move_map() { // 위에서부터 아래로 미로 이동 해주는 함수 
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 7; j++) {
			tmp[j + 1][i] = map[j][i];
		}
		tmp[0][i] = '.';
	}

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			map[i][j] = tmp[i][j];
		}
	}
}

bool solve() {
	queue<pair<int, int>> q;
	q.push({ 7,0 }); // x y

	while (!q.empty()) {
		int Size = q.size();
		
        while (Size--) { // 이동할 수 있는 모든 상황을 다 생각해야 하기 때문에 이 부분을 제거한다면 모든 경우의 수가 따져지지 않기 때문에 값이 틀리게 나올 수 있다. 
			int x = q.front().first;
			int y = q.front().second;
			q.pop();
			
			if (map[x][y] == '#') continue;
			if (x <= high) return true; // 가장 높이 있던 벽 이상높이(인덱스번호로는 이하)로 이동했을 경우 언젠간 도착할 수 있기 때문
			if (x == 0 && y == 7)return true;

			for (int i = 0; i < 9; ++i) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= 8 || ny < 0 || ny >= 8) continue;
				if (map[nx][ny] == '#') continue;
				q.push({ nx,ny });
			}
		}

		move_map();
		++high;
	}


	return false;
}

int main() {

	bool chk = true;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			cin >> map[i][j];
			if (map[i][j] == '#' && chk) { // 가장 높은 위치에 있는 벽을 확인하기 위해서 (high가 나을수록 높이 있다.)
				high = i;
				chk = false;
			}
		}
	}

	cout << solve();
	

	return 0;
}
