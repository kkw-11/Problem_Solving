def solution(n,a,b):
    answer = 0
    '''
    1 2 3 4 5 6 7 8
     1   2   3   4
       1       2
    '''
    for i in range(1,n//2):
        if a%2 == 0:
            if b == a-1:
                answer = i
                break
            else:
                a = a//2
        else:
            if b == a + 1:
                answer = i
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