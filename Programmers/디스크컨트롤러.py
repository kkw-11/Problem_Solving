#https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer, now, last = 0, 0, -1
    wait, n, count = [], len(jobs), 0

    while count < n:
        for job in jobs:
            if last < job[0] <= now:
                answer += (now - job[0])
                heapq.heappush(wait, job[1]) 

        if not wait:
            now += 1
            continue

        t = heapq.heappop(wait)
        answer += len(wait) * t
        last = now
        now += t
        count += 1

    return answer // n