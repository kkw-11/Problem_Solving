def solution(n):
    answer = 0
    exponent = 0
    def three_digit(x):
        reverse_number = 0
        digit = 1
        while x:
            x, mod = divmod(x,3)
            number = reverse_number + mod *digit
            digit *= 10
        else:
            return number
    
    temp = three_digit(n)
    for t in str(temp):
        answer += int(t)*3**exponent
        exponent += 1
    
    return answer