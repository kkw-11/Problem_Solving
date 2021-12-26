def solution(n):
    ans = 0
    
    # (현재까지 온 거리) x 2 에 해당하는 위치'로'
    # K 칸 점프
    # 정수 만큼 이동
    
    while n > 0:
        if n%2 == 0:
            n = n//2
        else:
            n -= 1
            ans +=1

    return ans