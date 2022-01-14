def solution(participant, completion):
    answer = ''
    completion_dict = {}
    for completion_player in completion:
        if not completion_player in completion_dict:
            completion_dict[completion_player] = 1
        else:
            completion_dict[completion_player] += 1
            
    for player in participant:
        if player in completion_dict and completion_dict[player] >= 1:
            completion_dict[player] -= 1
            continue

        if completion_dict.get(player) == 0 or completion_dict.get(player) == None:
            return player
                
