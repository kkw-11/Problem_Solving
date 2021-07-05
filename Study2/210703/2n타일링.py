import sys
sys.setrecursionlimit(60000) # 재귀 호출 범위를 늘려준다.

def solution(n):
    mem = [-1 for i in range(60001)] # 메모이제이션

    def dp(n):
        if mem[n] != -1: return mem[n]
        if n == 0: return 1 # 공집합도 1로본다
        if n == 1: return 1
        mem[n] = (dp(n-1) + dp(n-2)) % 1000000007
        return mem[n]

    return dp(n)
