//https://www.acmicpc.net/problem/16234
#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;

typedef struct position{
	int r, c;
}POSI;

int n, l, r;
int map[50][50];

void check_area(int sr, int sc, int area[][50],int index, int& count, int& sum) {
/*
다른 시작점에서는 동맹국이 아닐지 모르지만 지금 시작점에서 다시 동맹국으로 생길지 모르기 때문에 
main for문에서 매번 시작좌표로 함수를 호출할때 마다 모든 좌표 방문은 초기화 해주어 현재 시작 위치로부터 방문 했었은지 확인해야 한다.
*/
	int visited[50][50] = { 0, }; 

	const int dr[] = { -1, 1, 0, 0 };
	const int dc[] = { 0, 0, -1, 1 };

	//탐색진행 전 시작 좌표 start row, start coloum을 큐에 넣기 작업
	queue<POSI> q;
	POSI head; //head 라는 구조체 변수 선언
	head.r = sr;
	head.c = sc;
	visited[sr][sc] = 1;
	q.push(head);

	while (!q.empty()) {
		POSI cur = q.front();
		q.pop();

		area[cur.r][cur.c] = index;
		++count;
		sum += map[cur.r][cur.c];
		//현재 위치(r,c)에서 문제의 조건에 부합하는 상하좌우에 위치한 곳은 전부 큐에 넣기
		for (int dir = 0; dir < 4; ++dir) {
			POSI next;
			next.r = cur.r + dr[dir];
			next.c = cur.c + dc[dir];

			if (next.r < 0 || next.r >= n || next.c < 0 || next.c >= n) continue; //주어진 map에서 벗어난 위치이면 다음 방향 찾기

			int delta = abs(map[cur.r][cur.c] - map[next.r][next.c]); //절대값 차 구하기
			if (visited[next.r][next.c] == 0 && l <= delta && delta <= r) {
				visited[next.r][next.c] = 1;
				q.push(next);
			}
		}
	}
}


int main(){
	freopen("input.txt", "rt", stdin);

	scanf("%d %d %d", &n, &l, &r);
	for (int y = 0; y < n; ++y) {
		for (int x = 0; x < n; ++x) {
			scanf("%d", &map[y][x]);
		}
	}

	int result = 0;
	bool is_update = true;
	while (is_update) {
		is_update = false;

		int what_area[50][50] = { 0, };
		int area_index = 0;
		int count[2501] = { 0, };//50*50 = 2500개의 개별 국가 존재 가능
		int sum[2501] = { 0, };
		for (int r = 0; r < n; ++r) {
			for (int c = 0; c < n; ++c) {
				if (what_area[r][c] == 0) {
					++area_index;
					check_area(r, c, what_area, area_index, count[area_index], sum[area_index]);
				}
			}
		}

		for (int r = 0; r < n; ++r) {
			for (int c = 0; c < n; ++c) {
				int area_num = what_area[r][c];
				int avg = sum[area_num] / count[area_num];
				if (map[r][c] != avg) {
					map[r][c] = avg;
					is_update = true;
				}
			}
		}
		if (is_update) {
			++result;
		}
	}

	printf("%d\n", result);
	return 0;
}


//출처: https://na982.tistory.com/99 [na982]

///////////////////////////////////////////////////////////////////////////////////////
// 아래코드는 리패토링전 스터디 코드

// import sys
// import heapq
// import math
// from collections import deque
// sys.setrecursionlimit(100000)

// dx = [-1,1,0,0]
// dy = [0,0,-1,1]

// N,L,R = map(int,input().split())
// pp    = [list(map(int,input().split())) for _ in range(N)]
// cnt   = 0

// def go(x,y) :
//     totSum = pp[x][y]
//     totGrp = [(x,y)]
//     for k in range(4):
//         nx,ny = x+dx[k],y+dy[k]
//         if 0 <= nx < N and 0 <= ny < N :
//             if L <= abs(pp[nx][ny] - pp[x][y]) <= R and ch[nx][ny] == False :
//                 ch[nx][ny] = True
//                 tmpSum,tmpGrp = go(nx,ny)
//                 totSum += tmpSum
//                 totGrp += tmpGrp 
//     return totSum,totGrp

// while True:
//     change = False
    
//     ch    = [[False]*N for _ in range(N)]
//     befpp = [list(p) for p in pp]
    
//     for i in range(N):
//         for j in range(N):
//             if ch[i][j] == False:
//                 ch[i][j] = True
//                 psum,pgrp = go(i,j)
//                 pavg = math.floor(psum//len(pgrp))
//                 for gp in pgrp:
//                     x,y = gp
//                     pp[x][y] = pavg
//     for i in range(N):
//         for j in range(N):
//             if befpp[i][j] != pp[i][j]:
//                 change = True
//                 break
//     if not change :
//         break
//     cnt += 1
// print(cnt)