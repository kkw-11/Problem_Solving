def solution(nums):
    answer = 0
    half =  len(nums)//2
    number_of_poncketmons = len(set(nums))

    if number_of_poncketmons <= half:
        answer = number_of_poncketmons
    else:
        answer = half
        
    return answer