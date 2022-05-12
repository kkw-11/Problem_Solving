import sys

def recur(west, east):
    global checked, DP, n,m
    if west >=n:
        checked[west][east] = True
        DP[west][east] = 1
        return DP[west][east]
    else:
        for next_east in range(east+1, m+1):
            if not checked[west+1][next_east]:
                DP[west][east] += recur(west+1, next_east)
            else:
                DP[west][east] += DP[west+1][next_east]
        checked[west][east] = True
        return DP[west][east]

sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    DP = [[0]*(m+1) for _ in range(n+1)]
    checked = [[False]*(m+1) for _ in range(n+1)]
    for east in range(1,m+1-n +1):
        DP[1][east] += recur(1,east)
    print(sum(DP[1]))
