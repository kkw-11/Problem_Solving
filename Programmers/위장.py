def solution(clothes):
    answer = 1
    clothes_dict = {}
    for clothe in clothes:
        if not clothe[1] in clothes_dict:
            clothes_dict[clothe[1]] = [clothe[0]]
        else:
            clothes_dict[clothe[1]].append(clothe[0])
    
    for clothe_clasifi in clothes_dict:
        answer *= (len(clothes_dict[clothe_clasifi])+1)
        
    
    return answer-1