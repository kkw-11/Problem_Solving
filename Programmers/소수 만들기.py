def solution(nums):
    def isPrime(num):
        for n in range(2,num//2): 
            if num % n == 0:
                return False
        else:
            return True

    def combination(start, depth, total):
        nonlocal answer
        if depth == 2:
            if isPrime(total):
                answer += 1
            return
        else:
            for next in range(start+1,len(nums)):
                combination(next,depth+1,total+nums[next])

    answer = 0
    
    for start_index in range(len(nums)):
        combination(start_index,0,nums[start_index])

    return answer