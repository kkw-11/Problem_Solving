
num_teams = 3
remote_tasks =["development","marketing","hometask"]
office_tasks = 	["recruitment","education","officetask"]
employees = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]


from collections import deque
def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    remote_dic = {}
    office_dic = {}
    team_member = [[] for _ in range(num_teams+1)] 
    team_remote = [deque() for _ in range(num_teams+1)]
    
    for office_task in office_tasks:
        office_dic[office_task] = True

    for employee_num, employee in enumerate(employees):
        employee_lists = employee.split() # ["1", development, hometask]
        team_member[int(employee_lists[0])].append(employee_num+1)

        for task in employee_lists[1:]:
            if task in office_dic:
                break
        else:
            team_remote[int(employee_lists[0])].append(employee_num+1)

    for num_team in range(1,num_teams+1):
        if len(team_member[num_team]) != len(team_remote[num_team]):
            answer.extend(team_remote[num_team])
        else:
            team_remote[num_team].popleft() 
            answer.extend(team_remote[num_team])
    return answer



