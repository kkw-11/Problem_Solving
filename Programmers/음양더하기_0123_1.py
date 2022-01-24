def solution(absolutes, signs):
    answer = 0
    
    check ={True:1,False:-1}
    
    for index, value in enumerate(signs):
        answer = answer + (absolutes[index] * check[value])
    
    return answer