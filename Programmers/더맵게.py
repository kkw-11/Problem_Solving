import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if scoville[0] >= K:
            break
            
        first = heapq.heappop(scoville)

        if len(scoville) == 0:
            return -1
           
        second = heapq.heappop(scoville)
        mix = first + second*2
        heapq.heappush(scoville,mix)

        answer += 1
        
        
    return answer