# queue1,queue2 길이 같음, 합이 같게 하는 최소 연산햣 

from collections import deque

def solution(queue1, queue2):
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)
    initial_q1 = sum(q1)
    initial_q2 = sum(q2)
    sum_q1 = initial_q1
    sum_q2 = initial_q2
    len_q1 = len(queue1)
    len_q2 = len(queue2)


    if initial_q1 == initial_q2:
        return 0
    else:
        while True:
            if sum_q1 > sum_q2:
                sum_q1 -= q1[0]
                sum_q2 += q1[0]
                q2.append(q1.popleft())
                answer += 1
            elif sum_q1 < sum_q2:
                sum_q2 -= q2[0]
                sum_q1 += q2[0]
                q1.append(q2.popleft())
                answer += 1
            else:
                break

            if answer >= (len_q1 + len_q2):
                return -1

    return answer