def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    go_team = set()
    home_member = []
    go_member = []
    office_dict = {}
    for office_task in office_tasks:
        office_dict[office_task] = True
    for employee_num, employee_infos in enumerate(employees):
        emp_info = employee_infos.split()
        for task in emp_info[1:]:
            if task in office_dict:
                go_team.add(emp_info[0])
                break
        else:
            home_member.append((int(employee_num)+1,emp_info[0]))
    home_member.sort()
    for emp in home_member:
        if emp[1] not in go_team:
            go_team.add(emp[1])
        else:
            answer.append(emp[0])

    return answer