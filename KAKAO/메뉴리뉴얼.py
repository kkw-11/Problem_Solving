from itertools import combinations

def solution(orders, course):
    result = []
    
    for size_of_course in  course:
        course_menu_dict = {}
        
        for order in orders:
            all_course = list(map("".join,list(combinations(sorted(order),size_of_course))))
        
            for each_course in all_course:
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

# from itertools import combinations


# def solution(orders, course):
#     answer = []
#     order_list = []
 
#     for c in course:
#         order_dict = {}
#         for order in orders:
            
#             combies = list(map(''.join, list(combinations(sorted(order), c))))

#             for combi in combies:
#                 if combi in order_dict:
#                     order_dict[combi] += 1
#                     continue
#                 order_dict[combi] = 1
#         if len(order_dict) == 0:
#             continue
#         max_val = max(order_dict.values())
#         if max_val >= 2:
#             for key, value in order_dict.items():
#                 if value == max_val:
#                     answer.append(key)

#     answer = sorted(answer)

#     return answer
