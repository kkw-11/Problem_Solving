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
	queue<pair<int, int>> q; //(6.0) (6,1)
	q.push({ 7,0 }); // x y

	while (!q.empty()) {
		int Size = q.size();
		
        while (Size--) { // 이동할 수 있는 모든 상황을 다 생각해야 하기 때문에 이 부분을 제거한다면 모든 경우의 수가 따져지지 않기 때문에 값이 틀리게 나올 수 있다. 
			int x = q.front().first;
			int y = q.front().second;
			q.pop();
			
			if (map[x][y] == '#') continue;
			if (x <= high) return true; // 가장 높이 있던 벽 이상으로 이동했을 경우 언젠간 도착할 수 있기 때문
			if (x == 0 && y == 7)return true;

			for (int i = 0; i < 9; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= 8 || ny < 0 || ny >= 8) continue;
				if (map[nx][ny] == '#') continue;
				q.push({ nx,ny });
			}
		}

		move_map();
		high++;
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

// //스터디원 코드
// import sys
// import heapq
// import math
// import copy
// from collections import deque, defaultdict
// sys.setrecursionlimit(100000)

// dx = [-1,1,0,0,0,-1,-1,1,1]
// dy = [0,0,-1,1,0,1,-1,-1,1]

// # 이동할 수 있는지 없는지
// # 최소 bfs를 활용하기
// # 정점 정의 : d[r][c][t]
// # t 시점에 r,c 좌표에 , 정점 정보
// # 그렇다면, t의 범위는 어떻게 설정할 수 있을까 ?
// # t의 범위는 0~ 7 까지 -> 8초 후면 어차피 사라지므로
// # d 라는 배열을 따로 마련해야 하나 ? yes
// # 이를 통해서, 목적지까지 도달했는지 여부를 알 수 있다
// # 그냥 maps 자체에서 처리할 수 있지 않을까 ?
// maps = [list(input()) for _ in range(8)]
// dist = [[[-1]*8 for _ in range(8)] for _ in range(8)]

// # x,y,t
// q = deque()
// dist[7][0][0] = 0
// q.append((7,0,0))

// while q :
//     x,y,t = q.popleft()
//     for k in range(9):
//         nx,ny = x+dx[k],y+dy[k]
//         nt = min(7,t+1)
//         if 0 <= nx < 8 and 0 <= ny < 8 and dist[nx][ny][nt] == -1 :
//             # 현재 시점에,가려는 칸이 벽이면
//             if nx-t >= 0 and maps[nx-t][ny] == '#' : #t=2
//                 continue
//             # 1초후에, 벽이 내려오는 거라면
//             if nx-(t+1) >= 0 and maps[nx-(t+1)][ny] == '#' :
//                 continue
//             dist[nx][ny][nt] = dist[x][y][t] + 1
//             q.append((nx,ny,nt))

// res = 0
// for i in range(8):
//     if dist[0][7][i] != -1 :
//         print(1)
//         exit(0)
// print(res)