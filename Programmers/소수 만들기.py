def solution(nums):
    answer = 0

    def isPrime(num):
        if num == 1:
            return False
        else:
            for n in range(2,num//2 + 1):
                if num % n == 0:
                    return False
            else:
                return True

    def combi(start, depth, total):
        nonlocal answer
        if depth == 2:
            if isPrime(total):
                answer += 1
            return
        else:
            for next in range(start+1,len(nums)):
                combi(next,depth+1,total+nums[next])
        
    for start_index in range(len(nums)):
        combi(start_index,0,nums[start_index])
        

    return answer