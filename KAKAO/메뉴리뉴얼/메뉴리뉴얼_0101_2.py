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

    
    '''
    정렬 전 상태 ["XYZ", "XWY", "WXA"]

=> 정렬 후 상태["XYZ", "WXY", "AWX"]

[2,3,4]
max_val = 1
key = "XYZ", vaule =1

result = ["XY","WX" ]

course_menu_dict
횟수 2=> "XY":2, "XZ":1, "YZ":1 ,"WX":2, "WY":1, "AW":1, "AX":1
   v  3=> "XYZ":1, "WXY":1, "AWX":1
      4=> NULL

A. COURSE에서 숫자를 하나 뽑아서 체크 2, 3, 4 
  B. 뽑은 숫자 만큼 각 손님의 조합 메뉴 구하기
  C. 그 메뉴들의 주문횟수를 구해
  D. 가장 많이 합께 주문한 메뉴를 확인하고 그 메뉴가 무엇인지 RESULT에 저장해

2개 조합
1번 손님
 "XY", "XZ", "YZ" 
2번 손님
 "WX", "WY", "XY"
3번 손님
 "AW", "AX", "WX"



3개 조합
1번손님
 "XYZ"
2번손님
 "WXY"
3번손님
 "AWX"



4개 조합
1번손님
 NULL
2번손님
 NULL
3번손님
 NULL

    
    '''