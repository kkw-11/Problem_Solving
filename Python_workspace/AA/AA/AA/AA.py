def solution(citations):
    answer = 0 
    n = len(citations)
    citations.sort()

    for idx, value in enumerate(citations):
        if (n-idx) >= value and citations[idx-1]<=value: # n-idx : value 이상 인용된 논문수
            answer = value
        else:
            if idx>0:
                break

    return answer

citations = [3, 0, 6, 1, 5]

print(solution(citations))