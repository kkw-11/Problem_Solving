from itertools import combinations

def solution(orders, course):
    result = []
    for size_of_course in course:
        combis = []
        menu_cnt_dict = {}

        for order in orders:
            combis.extend(map("".join,combinations(sorted(order),size_of_course)))

        for combi in combis:
            if not combi in menu_cnt_dict:
                menu_cnt_dict[combi] = 1
            else:
                menu_cnt_dict[combi] += 1

        # max 함수 예외 처리
        if len(menu_cnt_dict) != 0:
            max_value = max(menu_cnt_dict.values())

            if max_value > 1:
                for key, value in menu_cnt_dict.items():
                    if value == max_value:
                        result.append(key)


    return sorted(result)