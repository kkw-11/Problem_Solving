from itertools import combinations

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

#for size_of_course in course:
#    print(size_of_course) 

result = []
for size_of_course in course:
    course_menu_dict = {}
    each_person_order_all = []
    
    for order in orders:
        each_person_order_all.extend(list(map("".join,combinations(sorted(order), size_of_course))))


    for each_course in each_person_order_all:
        if not each_course in course_menu_dict:
            course_menu_dict[each_course] = 1
        else:
            course_menu_dict[each_course] += 1

    if len(course_menu_dict) == 0:
        continue

    max_val = max(course_menu_dict.values())
    if max_val >= 2:
        for key, value in course_menu_dict.items():
            if value == max_val:
                result.append(key)
  
print(sorted(result))