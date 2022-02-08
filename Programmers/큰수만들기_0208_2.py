def solution(number, k):
    answer = ""
    cnt = 0
    for index, cur_num in enumerate(number):
        while len(answer) != 0 and answer[-1] < cur_num and cnt != k:  
            answer = answer[:-1]
            cnt += 1

        answer += cur_num
        if cnt == k:
            answer += number[index+1:]
            break
    while cnt < k:
        cnt += 1
        answer = answer[:-1]

    return answer