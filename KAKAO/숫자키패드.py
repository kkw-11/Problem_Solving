def solution(numbers, hand):
    answer = ''
    left_number = {1:True,4:True,7:True}
    right_number = {3:True,6:True,9:True}
    check_number = {2:True,5:True,8:True,0:True}
    number_where= {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),0:(3,1)}
    left_where = (0,3)
    right_where = (3,2)
    
    #현재 숫자 l,r check 숫자 확인
                
    # check 숫자면 현재 왼손 위치와 오른손 위치와의 거리 계산
    
    # 거리 같으면 hand 값 확인
    
    # 짧은 거리 손가락 사용
    for number in numbers:
        if number in check_number:
            #거리계산
            left_distance = abs(number_where[number][0] - left_where[0]) + abs(number_where[number][1] - left_where[1])
            right_distance = abs(number_where[number][0] - right_where[0]) + abs(number_where[number][1] - right_where[1]) 
            
            if left_distance == right_distance:
                if hand == "right":
                    answer += "R"
                    right_where = number_where[number]
                elif hand == "left":
                    answer += "L"
                    left_where = number_where[number]

            elif left_distance > right_distance:
                answer += "R"
                right_where = number_where[number]
            elif left_distance < right_distance:
                answer += "L"
                left_where = number_where[number]
        elif number in left_number:
            answer += "L"
            left_where = number_where[number]
        elif number in right_number:
            answer += "R"
            right_where = number_where[number]
    
    return answer