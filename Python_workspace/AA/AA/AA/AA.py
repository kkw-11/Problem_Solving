import sys 
#sys.stdin = open("input.txt","rt")

def solution(n, results):
    answer = 0
    playerInfos = [[0,0,0,0] for _ in range(n+1)] # (승,패,경기수,순위)
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]

    for result in results:
        for i in range(2):
            if i == 0:  # 승 result[i]는 승리한 player 번호
                playerInfos[result[i]][0] += 1 # 승 수
                playerInfos[result[i]][2] += 1 # 경기수
            else: # 패 result[i]는 패배한 player 번호
                playerInfos[result[i]][1] += 1 # 패 수
                playerInfos[result[i]][2] += 1 # 경기수
                

    for i in range(1,n+1):
        if playerInfos[i][2] == n-1:
                answer += 1


             
    for playerInfo in playerInfos:
           if playerInfo[2] == n-1: # 나머지 선수와 모두 경기 했다면
                answer += 1
                playerInfo[3] = n - playerInfo[0] # 1승이라면 4위 (5-1) 꼴지에게만 이김
                for result in results:
                    for j in range(2):
                        if result[j] == player and j == 0:
                            answer += 1
           elif playerInfos[player][3] == 2:
               for result in results:
                   for j in range(2):
                       if result[j] == player and j == 1:
                           answer += 1


    for player in range(1,n+1):
        if playerInfos[player][3] == n-1:
            for result in results:
                for j in range(2):
                    if result[j] == player and j == 0:
                        answer += 1
        elif playerInfos[player][3] == 2:
            for result in results:
                for j in range(2):
                    if result[j] == player and j == 1:
                        answer += 1
                        
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

answer = solution(n,results)

print(answer)

