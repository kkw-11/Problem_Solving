def solution(nums):
    answer = 0
    half = len(nums)//2
    poncketmon_category_list = []
    cnt = 0
    poncketmon_category_cnt = 0
    
    for num in nums:
        if num in poncketmon_category_list:
            continue
        else:
            poncketmon_category_list.append(num)
            
    poncketmon_category_cnt = len(poncketmon_category_list)
    
    
    if poncketmon_category_cnt < half:
        return poncketmon_category_cnt
    else:
        return half
    
    

