

def solution(n):
    answer = 0
    exponent = 0 
    result = 0
    def reverse_three_digit(x):
        res = 0
        while x:
            x, mod = divmod(x,3)
            res = res*10 + mod
        else:
            return res
    
    temp = reverse_three_digit(n)
    while temp:
        temp, mod = divmod(temp,10)
        result += (mod*(3**exponent))
        exponent += 1
        
    
    
    
    return result