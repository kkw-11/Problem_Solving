def solution(n):
    answer = 0
    exponent = 1 
    result = 0
    def reverse_three_digit(x):
        res = []
        while x:
            x, mod = divmod(x,3)
            res.append(mod)
        else:
            return res
    
    temp = reverse_three_digit(n)
    for mod in temp[::-1]:
        result += (mod * exponent)
        exponent *= 3
    
    return result