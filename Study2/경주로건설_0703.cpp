#include <bits/stdc++.h>
 
using namespace std;
 
class Car{
    public:
    int x,y,cost, dir;
};
 
int solution(vector<vector<int>> board) {
    int answer = 999999999, mx[] = {0,1,0,-1}, my[] = {1,0,-1,0}, N = board.size();
    queue<Car> q;    
    Car c;
    c.x = 0, c.y = 0, c.cost = 0, c.dir = 10;
    q.push(c);
    board[0][0] = 1;
    
    while(!q.empty())
    {
        Car a = q.front();
        q.pop();
        if(a.x == N - 1 && a.y == N - 1)
        {
            if(answer > a.cost) answer = a.cost;
            continue;
        }
        for(int i=0;i<4;i++)
        {
            int nx = a.x + mx[i];
            int ny = a.y + my[i];
            
            if( nx<0 || ny<0 || nx>=N || ny>=N || board[nx][ny] == 1) continue;
            
            int nc = 0;
            
            if(a.dir == 10 || a.dir == i)
                nc = a.cost + 100;
            else if(a.dir != i)
                nc = a.cost + 600;
            
            if(board[nx][ny] == 0 || board[nx][ny] >= nc)
            {
                board[nx][ny] = nc;
                Car p;
                p.x = nx, p.y = ny, p.cost = nc, p.dir = i;
                q.push(p);
            }
        }
        
    }
    return answer;
}



// from collections import deque

// def solution(board):
//     dX = [1, -1, 0, 0]
//     dY = [0, 0, 1, -1]
//     queue = deque([])
//     queue.append((0, 0, 0, 0))  # 좌표, 방향
//     valueBoard = list([0] * len(board) for _ in range(len(board)))

//     while queue:
//         x, y, car_d, value = queue.popleft()
//         for road_d in range(4):  # 동 서 남 북 방향
//             nX = x + dX[road_d]
//             nY = y + dY[road_d]

//             if 0 <= nX < len(board) and 0 <= nY < len(board):
//                 if board[nY][nX] != 1:
//                     if nX == 0 and nY == 0:
//                         continue
    
//                     if x == 0 and y == 0:
//                         newValue = value + 100
//                     else:
//                         if car_d == road_d:
//                             newValue = value + 100
//                         else:
//                             newValue = value + 600

//                     if valueBoard[nY][nX] == 0:
//                         valueBoard[nY][nX] = newValue
//                         queue.append((nX, nY, road_d, newValue))
//                     else:
//                         if valueBoard[nY][nX] >= newValue:
//                             valueBoard[nY][nX] = newValue
//                             queue.append((nX, nY, road_d, newValue))


//     return valueBoard[-1][-1]