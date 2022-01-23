def next_round_number(a,b):
    next = [a//2+a%2, b//2+b%2]
    
    return next

def solution(n,a,b):
    answer = 1
    
    next_number = next_round_number(a,b)
    
    while True:
        if next_number[0] == next_number[1]:
            break
        answer+=1

        next_number= next_round_number(next_number[0], next_number[1])

    return answer