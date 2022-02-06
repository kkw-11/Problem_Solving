def solution(nums):
    answer = 0
    half = len(nums)//2
    poncketmon_dict = {}
    cnt = 0
    number_of_poncketmon_category = 0
    

    for num in nums:
        if not num in poncketmon_dict:
            poncketmon_dict[num] = True
        else:
            poncketmon_dict[num] += 1
            
    poncketmon_list = list(poncketmon_dict.keys())
    number_of_poncketmon_category = len(poncketmon_list)
    
    
    if number_of_poncketmon_category < half:
        return number_of_poncketmon_category
    else:
        return half
    
    
        
        

