def solution(line):
    answer = []
    left = [1,0]
    right = [1,9]
    qwerty = [['1', '2', '3', '4', '5','6', '7', '8', '9', '0'],
              ['Q', 'W', 'E', 'R', 'T','Y', 'U', 'I', 'O', 'P']
            ]
    qwerty_dict = {'1':(0,0), '2':(0,1), '3':(0,2), '4':(0,3),'5':(0,4),'6':(0,5),'7':(0,6),'8':(0,7),'9':(0,8),'0':(0,9),'Q':(1,0), 'W':(1,1), 'E':(1,2), 'R':(1,3),'T':(1,4),'Y':(1,5),'U':(1,6), 'I':(1,7), 'O':(1,8), 'P':(1,9) }
    
    for ch in line:
        row, col = qwerty_dict[ch]
        lef_row_dis = abs(left[0] - row)
        lef_col_dis = abs(left[1] - col)

        ri_row_dis = abs(right[0] - row)
        ri_col_dis = abs(right[1] - col)

        left_men = (lef_col_dis + lef_col_dis)
        right_men = (ri_row_dis + ri_col_dis)
        if left_men < right_men:
            answer.append(0)
            left = [row,col]
        elif left_men > right_men:
            answer.append(1)
            right = [row,col]
        else:
            if lef_col_dis < ri_col_dis:
                answer.append(0)
                left = [row,col]
            elif lef_col_dis > ri_col_dis:
                answer.append(1)
                right = [row,col]
            else:
                if ch in ('1', '2', '3', '4', '5', 'Q', 'W', 'E', 'R', 'T'):
                    answer.append(0)
                    left = [row,col]
                else:
                    answer.append(1)
                    right = [row,col]

    return answer