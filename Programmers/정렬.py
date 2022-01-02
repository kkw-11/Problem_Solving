def solution(numbers):
    numbers_str = list(map(str,numbers))
    
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers_str[j] + numbers_str[j+1] < numbers_str[j+1] + numbers_str[j]:
                numbers_str[j+1] , numbers_str[j] = numbers_str[j] , numbers_str[j+1] 
    
    return str(int("".join(numbers_str)))