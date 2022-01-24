def solution(nums):

    '''
    
    7 -> 2 

    16

    1 * 16
    2 * 8

    4 * 4

    8 * 2
    16 * 1

    '''

    def isPrime(num):
        if num > 1:
            for n in range(2, int(num**0.5)+1): 
                if num % n == 0:
                    return False
            else:
                return True
        else:
            return False

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

    return answerㅎ