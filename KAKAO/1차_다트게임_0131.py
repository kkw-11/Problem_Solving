def solution(dartResult):
    answer = 0
    scores = [None]*3
    game_round = 0
    BONUS = ["S","D","T"]
    OPTION = ["*","#"]
    
    
    for dart in dartResult:
        if dart in "0123456789":
            if scores[game_round] == None:
                scores[game_round] = int(dart)
            else:
                scores[game_round] = scores[game_round]*10 + int(dart)
        
        if dart in BONUS:
            if dart == BONUS[1]:
                scores[game_round] = scores[game_round]**2
            elif dart == BONUS[2]:
                scores[game_round] = scores[game_round]**3
                
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