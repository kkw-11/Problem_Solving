def solution(nums):
    answer = 0
    
    if len(set(nums)) <= len(nums)//2:
        answer = len(set(nums))
    else:
        answer = len(nums)//2
        
    return answer