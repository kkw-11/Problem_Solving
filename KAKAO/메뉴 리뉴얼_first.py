from itertools import combinations

def solution(orders, course):
    result = []

    for size_of_course in  course:
        course_menu_dict = {}

        for order in orders:
            all_course = list(combinations(sorted(order),size_of_course))

            for each_course in all_course:
                each_course_str = "".join(each_course)
                if not each_course_str in course_menu_dict:
                    course_menu_dict[each_course_str] = 1
                else:
                    course_menu_dict[each_course_str] += 1
        else:
            max_cnt = 0
            course_menu = None
            cnt_dict = {}
            for c in course_menu_dict:
                if course_menu_dict[c] >= 2:
                    if not course_menu_dict[c] in cnt_dict:
                        cnt_dict[course_menu_dict[c]] = [c]
                    else:
                        cnt_dict[course_menu_dict[c]].append(c)
                    if max_cnt < course_menu_dict[c]:
                        max_cnt = course_menu_dict[c]
            else:
                if max_cnt != 0:
                    for cc in cnt_dict[max_cnt]:
                        result.append(cc)

    result.sort()


    return result