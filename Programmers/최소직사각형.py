def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    for index in range(len(sizes)):
        if sizes[index][0] < sizes[index][1]:
            sizes[index] = [sizes[index][1], sizes[index][0]]
        
        if max_width < sizes[index][0]:
            max_width = sizes[index][0]
        if max_height < sizes[index][1]:
            max_height = sizes[index][1]
            
    return max_width*max_height