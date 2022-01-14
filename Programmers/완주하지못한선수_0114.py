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

        if (player in completion_dict and completion_dict[player] == 0) or not player in completion_dict:
            return player
                
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         # dic 변수에 참가자 한명한명을 hash()를 통해 변환한 숫자를 key로, 참가자를 value로 설정 
#         dic[hash(part)] = part
#         # temp 변수에 참가자 모두를 합한 hash 숫자를 할당한다.
#         temp += int(hash(part))
#     # temp 변수에 있는 값에서 완주자 모두를 합한 hash 숫자를 뺀 뒤 그 값을 다시 temp에 할당한다. 
#     for com in completion:
#         temp -= hash(com)
#     # '참가자 전원의 hash 숫자 합 - 완주자 전원의 hash 숫자 합'을 key로 갖고 있는 dic의 value를 answer에 할당한다.
#     answer = dic[temp]

#     return answer