def solution(p):
    n = len(p)
    answer = [0]*n
    i = 0

    while i < n:
        min_data = float("inf")
        min_data_index = 0
        for j in range(i,n):
            if p[j] < min_data:
                min_data = p[j]
                min_data_index = j

        if i != min_data_index:
            p[i],p[min_data_index] = p[min_data_index], p[i]
            answer[i] += 1
            answer[min_data_index] += 1

        i += 1


    return answer 