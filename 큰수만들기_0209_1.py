def solution(number, k):
    answer = ""
    deleted_cnt = 0
    for index, cur_num in enumerate(number):
        while len(answer) != 0 and answer[-1] < cur_num and deleted_cnt < k:
            answer = answer[:-1]
            deleted_cnt += 1
        answer += cur_num
            
    if deleted_cnt < k:
        answer = answer[:-(k-deleted_cnt)]
        
    return answer