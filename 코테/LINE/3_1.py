def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    go_team = set()
    sub_home_member = []
    go_member = []
    office_dict = {}
    # 입력으로 주어진 자료구조 변형(문자열을 원소로 같는 리스트 -> 딕셔너리)
    for office_task in office_tasks:
        office_dict[office_task] = True

    # 알고리즘
    #재택근무후보 팀원과 출근하는 팀원 구하기
    for employee_num, employee_infos in enumerate(employees):
        emp_info = employee_infos.split()
        for task in emp_info[1:]:
            if task in office_dict:
                go_team.add(emp_info[0])
                break
        else:
            sub_home_member.append((int(employee_num)+1,emp_info[0]))
    # 출근하는 팀원이 아무도 없는 팀은 앞번호가 제거되어야 재택근무자 추려내기 위한 체크 전에 정렬
    sub_home_member.sort()

    # 재택근무자 후보중에 진짜 재택근무자 추려내기
    ## 재택 근무자 후보중에서 제외되어야 할 사람은 아무도 출근하지 않는 경우이다.
    ## 위에서 구한 출근하는 팀번호에 우리팀이 있는지 체크해서 없으면 우리팀 출근팀에 넣고 나는 재택근무자에서 빠진다.(여기서 빠진다는 answer 값에 들어가지 않는다.는 의미이다.)
    
    for emp in sub_home_member:
        if emp[1] not in go_team:
            go_team.add(emp[1])
        else:
            answer.append(emp[0])

    return answer