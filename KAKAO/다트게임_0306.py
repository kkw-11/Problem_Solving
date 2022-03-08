def solution(dartResult):
    answer = 0
    scores = [None]*3
    game_round = 0
    BONUS_DICT = {"S":1,"D":2,"T":3}
    OPTION = ["*","#"]
    
    
    for dart in dartResult:
        if dart in "0123456789":
            if scores[game_round] == None:
                scores[game_round] = int(dart)
            else:
                scores[game_round] = scores[game_round]*10 + int(dart)
        
        if dart in BONUS_DICT.keys():
            scores[game_round] = scores[game_round]**BONUS_DICT[dart]
                
            game_round += 1
    
        if dart in OPTION:
            game_round -= 1
            
            if game_round == 0 and dart == OPTION[0]:
                scores[game_round] = scores[game_round]*2
            elif game_round != 0 and dart == OPTION[0]:
                scores[game_round] = scores[game_round]*2
                scores[game_round-1] = scores[game_round-1]*2
                
            if dart == OPTION[1]:
                scores[game_round] = -scores[game_round]
                
            game_round += 1
    
    
    return sum(scores)