def solution(n, plans, clients):
    answer = []
    plan_dict = {}
    pre_service = set()
    for plan in plans:
        plan_list = plan.split(" ")

        plan_dict[plan_list[0]] = pre_service.union(plan_list[1:])
        pre_service = plan_dict[plan_list[0]]


    for client in clients:
        client_list = client.split(" ")

        for index, plan in enumerate(plans):
            plan_list = plan.split(" ")
            if int(plan_list[0]) >= int(client_list[0]):
                if plan_dict[plan_list[0]].intersection(set(client_list[1:])) == set(client_list[1:]):
                    answer.append(index+1)
                    break
        else:
            answer.append(0)


    return answer