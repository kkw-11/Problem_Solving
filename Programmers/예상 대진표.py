def solution(n,a,b):
    answer = 0
    for round in range(1,n//2):
        if a%2 == 0:
            if b == a - 1:
                answer = round
                break
            else:
                a = a//2
        else:
            if b == a + 1:
                answer = round
                break
            else:
                a = (a+1)//2

        if b%2 == 0:
            b = b//2
        else:
            b = (b+1)//2
    else:
        answer = n//2

    return answer