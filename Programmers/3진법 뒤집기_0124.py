def solution(n):
    answer = 0
    exponent = 1 
    def reverse_three_digit(x):
        reverse_number = 0
        while x:
            x, mod = divmod(x,3)
            reverse_number = reverse_number*10 + mod
        else:
            return reverse_number
    
    temp = reverse_three_digit(n)
    while temp:
        temp, mod = divmod(temp,10)
        answer += (mod*exponent)
        exponent *= 3
    
    return answer