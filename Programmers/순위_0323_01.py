from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])
    print(win)
    print(lose)
    for i in range(1, n + 1):
        for loser in win[i]: 
            lose[loser].update(lose[i])
        for winner in lose[i]: #i = 2 lose[2] : {1,3,4} win[2] : {5}
            win[winner].update(win[i])
   
    print("--------------------------------")
    print(win)
    print(lose)
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer
