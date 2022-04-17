def solution(skill, skill_trees):
    answer = 0
    requried_level = {}
    level = 0
    
    for level, sk in enumerate(skill):
        requried_level[sk] = level
    
    for skill_tree in skill_trees:
        level = 0
        for cur_skill in skill_tree:
            if not cur_skill in requried_level:
                continue
            else:
                if requried_level[cur_skill] > level:
                    break
                else:
                    level += 1
        else:
            answer += 1
                    
    return answer
