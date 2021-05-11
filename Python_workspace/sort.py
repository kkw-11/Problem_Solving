# 리스트 nums를 넣었을 때, 최댓값을 반환(return)하는 함수 our_max를 작성해봅시다.
# def our_max(nums)
#     nums.sort()
#     return a[-1]


def our_max(nums):
    maxNum = -99999999
    for i in nums:
        if i>maxNum:
            maxNum = i
    
    return maxNum

# 
print(our_max([1, 2, 10, 9, 3, 7, 0, 99, 27, 85]))