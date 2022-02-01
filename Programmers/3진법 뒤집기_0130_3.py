def solution(n):
    exponent = 1 
    
    def reverse_three_digit(x):
        reverse_number = 0
        while x:
            x, mod = divmod(x,3)
            reverse_number = reverse_number*10 + mod
        else:
            return reverse_number
     
    temp = reverse_three_digit(n)
    
    return int(str(temp),3)