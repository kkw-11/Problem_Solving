def solution(number, k):
    answer = ""
    for index, cur_num in enumerate(number):
        while len(answer) != 0 and answer[-1] < cur_num and k > 0:
            answer = answer[:-1]
            k -= 1
        answer += cur_num
            
    if k > 0:
        answer = answer[:-k]
        
    return answer