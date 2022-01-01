from itertools import combinations

def solution(orders, course):
    result = []
    
    for size_of_course in course:
        course_menu_dict = {}
        
        for each_person_order in orders:
            each_person_order_all_combi = list(map("".join, combinations(sorted(each_person_order),size_of_course)))
        
            for each_course in each_person_order_all_combi:
                if not each_course in course_menu_dict:
                    course_menu_dict[each_course] = 1
                else:
                    course_menu_dict[each_course] += 1

        else:
            if len(course_menu_dict) == 0:
                continue
            max_val = max(course_menu_dict.values())
            if max_val >= 2:
                for key, value in course_menu_dict.items():
                    if value == max_val:
                        result.append(key)
    result.sort()

    return result