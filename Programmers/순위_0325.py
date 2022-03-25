def solution(n, results):
    answer = 0
    win = [set() for _ in range(n+1)]
    lose = [set() for _ in range(n+1)]
    game_cnt = [0]*(n+1)
    for result in results:
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])

    for i in range(1,n+1):
        for loser in win[i].copy():
            win[i].update(win[loser])
        print(win[i])
        for winner in lose[i].copy():
            lose[i].update(lose[winner])
        print(lose[i])
        
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1

    return answer