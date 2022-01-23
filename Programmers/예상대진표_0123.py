def next_number_func(a,b):
    
    return [sum(divmod(a,2)), sum(divmod(b,2))]

def solution(n,a,b):
    answer = 1
    
    next_number = next_number_func(a,b)
    
    while True:
        if next_number[0] == next_number[1]:
            break
            
        answer+=1

        next_number = next_number_func(next_number[0], next_number[1])

    return answer