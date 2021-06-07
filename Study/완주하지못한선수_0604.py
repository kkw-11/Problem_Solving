# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    for p in participant:
        cnt = 0
        for c in completion:
            if p == c:
                completion.remove(c)
                break
            else:
                cnt += 1
        else:
            answer = p
            break
                
    return answer