from collections import defaultdict

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    report_info = defaultdict(set)
    cnt_info = defaultdict(int)
    
    number_of_user = len(id_list)
    who = []
    
    for value in report:
        user_info = value.split()
        
        report_info[user_info[0]].add(user_info[1])
        

        
    for i in range(number_of_user):
        for user in list(report_info[id_list[i]]):
            cnt_info[user] += 1
            
    for i in range(number_of_user):
        if cnt_info[id_list[i]] >= k:
            who.append(id_list[i])
    
    for i in range(number_of_user):
        for user in list(report_info[id_list[i]]):
            if user in who:
                answer[i] += 1
        
    
    return answer