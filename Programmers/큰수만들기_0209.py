def solution(number, k):
    answer = ""
    deleted_cnt = 0
    for index, cur_num in enumerate(number):
        if deleted_cnt < k:
            while len(answer) != 0 and answer[-1] < cur_num:
                answer = answer[:-1]
                deleted_cnt += 1
                if deleted_cnt >= k:
                    break
            answer += cur_num
        else:
            answer += number[index:]
            break
            
    if deleted_cnt < k:
        answer = answer[:-(k-deleted_cnt)]
        
    return answer